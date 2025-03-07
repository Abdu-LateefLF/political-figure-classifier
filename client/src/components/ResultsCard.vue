<script setup lang="ts">
import type { Classification } from '@/App.vue'
import politicians from '@/data/politicians'
import { computed } from 'vue'

const { classification } = defineProps<{
  classification: Classification | null
}>()

const img_url = computed(() => {
  if (!classification) return ''
  const politician = politicians.find((val) => val.name === classification.label)
  return politician ? politician.url : ''
})

const probabilities = computed(() => {
  if (!classification) return []
  return Object.keys(classification.label_dict).map((key, index) => ({
    name: key,
    probability: Math.round(classification.label_probability[index] * 100) / 100,
  }))
})
</script>

<template>
  <div
    v-if="classification"
    class="bg-white rounded-lg shadow-md p-4 w-full sm:w-96 transition-all duration-300 hover:shadow-lg"
  >
    <div class="flex flex-col sm:flex-row items-center space-x-4">
      <!-- Image -->
      <img
        :src="img_url"
        alt="Person Image"
        class="w-24 h-24 rounded-full object-cover border-2 border-gray-100"
      />

      <div class="flex-1 min-w-0 w-full">
        <h2 class="text-center sm:text-start text-xl font-semibold text-gray-900 truncate mb-2">
          {{ classification.label }}
        </h2>
        <ul class="space-y-2">
          <li
            v-for="(prob, index) in probabilities"
            :key="index"
            class="flex items-center justify-between"
          >
            <span class="text-sm font-medium text-gray-600 w-32 text-left">{{ prob.name }}</span>
            <div class="flex-1 bg-gray-100 rounded-full h-2 relative">
              <div
                :style="{ width: prob.probability + '%' }"
                class="absolute top-0 left-0 h-full bg-blue-500 rounded-full"
              ></div>
            </div>
            <span class="text-sm text-gray-700 w-8 text-right">{{ prob.probability }}%</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <div v-else class="text-gray-500 italic">No classification data available.</div>
</template>
