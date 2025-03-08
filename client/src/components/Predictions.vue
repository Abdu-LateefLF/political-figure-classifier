<script setup lang="ts">
import type { Classification } from '@/App.vue'
import ResultsCard from './ResultsCard.vue'

defineProps<{
  results: Classification[] | null
}>()
</script>

<template>
  <div class="container mx-auto mt-8 px-4">
    <div class="flex justify-center w-full">
      <h1 class="text-3xl font-bold text-gray-800">Predictions</h1>
    </div>

    <div
      v-if="results && results.length > 0"
      class="flex justify-center scroll-auto space-x-4 py-2 w-full"
    >
      <ResultsCard v-for="(res, index) in results" :key="index" :classification="res" />
    </div>
    <div v-else class="text-gray-500 italic text-center">No predictions available.</div>
  </div>
</template>
