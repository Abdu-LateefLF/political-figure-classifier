<script setup lang="ts">
import PersonCard from './components/PersonCard.vue'
import ImageUpload from './components/ImageUpload.vue'
import Predictions from './components/Predictions.vue'
import politicians, { type Politician } from './data/politicians'
import { ref } from 'vue'

export interface Classification {
  label: string
  label_dict: { [key: string]: number }
  label_probability: number[]
}

const people = politicians
const classificationRes = ref<Classification[]>([])

const handleClassification = (data: Classification[]) => {
  classificationRes.value = data
}
</script>

<template>
  <h1
    class="text-xl font-bold text-center my-8 bg-gradient-to-r from-blue-500 to-red-500 bg-clip-text text-transparent"
  >
    Political Figure Classifier
  </h1>

  <div class="flex flex-col-reverse md:flex-col">
    <div class="flex flex-wrap justify-center gap-6">
      <PersonCard
        v-for="person in people"
        :key="person.name"
        :name="person.name"
        :url="person.url"
        :facts="person.fact"
      />
    </div>

    <div class="mt-6 flex flex-col items-center justify-center md:flex-row w-full">
      <div class="md:w-1/2 pr-4 mb-4 md:mb-0">
        <ImageUpload @classification-done="handleClassification" />
      </div>
      <div class="w-full md:w-1/2">
        <Predictions :results="classificationRes" />
      </div>
    </div>
  </div>
</template>
