<template>
  <button v-show="visible" @click="scrollTop" class="back-top">↑</button>
</template>

<script setup>
import { ref, onMounted } from 'vue'
const visible = ref(false)
const scrollTop = () => { window.scrollTo({ top: 0, behavior: 'smooth' }) }
onMounted(() => { window.addEventListener('scroll', () => { visible.value = window.scrollY > 200 }) })
</script>

<style scoped>
/* Estilos BackToTop */
</style>