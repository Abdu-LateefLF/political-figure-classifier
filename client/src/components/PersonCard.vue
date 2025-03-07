<script setup lang="ts">
const props = defineProps<{
  name: string
  url: string
}>()
</script>

<template>
  <div
    class="bg-white rounded-lg p-3 w-48 transition-all duration-200 hover:shadow-lg hover:scale-105"
  >
    <img
      :src="url"
      alt="Person Image"
      class="w-32 h-32 rounded-full object-cover border-2 border-gray-100 mx-auto"
    />
    <div class="mt-2 text-lg font-semibold text-gray-800 text-center">{{ name }}</div>
    <div class="w-full h-1 rounded-md bg-blue-400/15 mt-6"></div>
  </div>
</template>
