<script setup lang="ts">
defineProps<{ name: string; url: string; facts: string }>()
</script>

<template>
  <div class="bg-white rounded-lg p-2 w-36 hover:scale-105 transition-all">
    <div class="h-28 hover:h-45 transition-all overflow-hidden">
      <img :src="url" :alt="name" class="w-20 h-20 rounded-full object-cover mx-auto" />
      <div class="mt-3 mb-3 text-[12px] font-medium text-center">{{ name }}</div>

      <p class="text-center text-[10px]">{{ facts }}</p>
    </div>
    <div class="w-full h-px bg-blue-200 mt-2 hover:bg-blue-500 hover:shadow-md"></div>
  </div>
</template>
