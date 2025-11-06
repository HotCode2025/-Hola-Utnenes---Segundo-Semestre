<script setup>
defineOptions({ name: 'EstudiosSection' })
import { ref } from 'vue'

const arreglo = ref([
    { id: 1, texto: 'Tecnicatura en Programación - En curso' },
    { id: 2, texto: 'Curso de Desarrollo Web - 2023' }
])
</script>

<template>
 <section id="estudios">
 <h2>Estudios</h2>
 <ul>
  <li v-for="item in arreglo" :key="item.id">
   {{ item.texto }}
  </li>
 </ul>
</section>
 </template>

<style scoped>

</style>
