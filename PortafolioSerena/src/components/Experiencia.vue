<script setup>
defineOptions({ name: 'ExperienciaSection' })
import { ref } from 'vue'

const experiencias = ref([
  { id: 1, texto: '2024 - Sitio para diario digital local' },
  { id: 2, texto: '2023 - Proyecto freelance: sitio para emprendimiento local' }
])
</script>

<template>
  <section id="experiencia">
    <h2>Experiencia</h2>
    <ul>
      <li v-for="exp in experiencias" :key="exp.id">{{ exp.texto }}</li>
    </ul>
  </section>
</template>

<style scoped>

</style>
