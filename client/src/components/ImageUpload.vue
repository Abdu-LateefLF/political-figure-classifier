<script setup lang="ts">
import { ref, defineEmits } from 'vue'
import { type Classification } from '../App.vue'

const emit = defineEmits(['classification-done'])

const imageFile = ref<File | null>(null)
const imageUrl = ref<string | null>(null)
const isClassifying = ref(false)
const errorMessage = ref<string | null>(null) // Add error message ref

const handleDrop = (event: DragEvent) => {
  event.preventDefault()
  const files = event.dataTransfer?.files
  if (files && files.length > 0) {
    processFile(files[0]) // Only process the first file
  }
}

const handleFileChange = (event: Event) => {
  const files = (event.target as HTMLInputElement).files
  if (files && files.length > 0) {
    processFile(files[0]) // Only process the first file
  }
}

const processFile = (file: File) => {
  if (!file.type.startsWith('image/')) return

  imageFile.value = file // Store the file
  const reader = new FileReader()
  reader.onload = () => {
    imageUrl.value = reader.result as string // Convert to base64 for preview
  }
  reader.readAsDataURL(file)
}

const preventDefault = (event: Event) => event.preventDefault()

const removeImage = () => {
  imageFile.value = null
  imageUrl.value = null
  errorMessage.value = null
}

// Make a call to the server to attempt to classify the image
const classifyImage = async () => {
  console.log('Classifying image...')

  const url =
    'https://political-figure-classifier-c6a9cufwa2gmcyhn.canadacentral-01.azurewebsites.net/classify'
  errorMessage.value = null // Clear any previous error message

  if (imageUrl.value) {
    isClassifying.value = true // Disable the button
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image_data: imageUrl.value }), // Send base64 encoded image
      })

      if (!response.ok) {
        const errorData = await response.json()
        if (errorData && errorData.error) {
          errorMessage.value = errorData.error
        } else {
          errorMessage.value = `Target is not clear in this image`
        }
        return
      }

      const data = (await response.json()) as Classification[]
      emit('classification-done', data)

      console.log(data)
    } catch (error) {
      console.error('Some issue occurred:', error)
      errorMessage.value = `Target is not clear in this image`
    } finally {
      isClassifying.value = false // Re-enable button
    }
  } else {
    console.warn('No image to classify.')
  }
}
</script>

<template>
  <div class="flex justify-center items-center my-6">
    <div>
      <div
        class="relative border-2 border-dashed border-gray-400 rounded-xl p-4 flex flex-col items-center justify-center cursor-pointer bg-white shadow-lg hover:shadow-xl transition w-full max-w-md h-48"
        @dragover="preventDefault"
        @dragenter="preventDefault"
        @drop="handleDrop"
      >
        <input
          type="file"
          accept="image/*"
          class="hidden"
          id="fileInput"
          @change="handleFileChange"
        />

        <label for="fileInput" class="h-full flex flex-col items-center justify-center">
          <div v-if="imageUrl" class="relative w-full h-full">
            <img
              :src="imageUrl"
              alt="Uploaded Image"
              class="w-full h-full object-cover rounded-xl"
            />

            <button
              @click.stop="removeImage"
              class="absolute top-3 right-3 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center shadow-md hover:bg-red-600 transition"
            >
              <i class="pi pi-times text-lg"></i>
            </button>
          </div>

          <div v-if="!imageUrl" class="text-gray-600 text-lg font-medium text-center">
            <p>Drag & Drop an image</p>
            <p>or</p>
            <span class="text-blue-500 font-semibold underline cursor-pointer"
              >Click to Upload</span
            >
          </div>
        </label>
      </div>

      <div v-if="errorMessage" class="text-red-500 mt-2 text-center">
        {{ errorMessage }}
      </div>

      <div v-if="imageUrl" class="mt-4 w-full flex justify-center">
        <button
          @click="classifyImage"
          class="w-40 py-2 px-4 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600 transition flex items-center justify-center"
          :disabled="isClassifying"
          :class="{ 'opacity-50 cursor-not-allowed': isClassifying }"
        >
          <template v-if="isClassifying">
            <i class="pi pi-spin pi-spinner mr-2"></i>
            Processing...
          </template>
          <template v-else> Classify </template>
        </button>
      </div>
    </div>
  </div>
</template>

<style>
@import 'primeicons/primeicons.css';
</style>
