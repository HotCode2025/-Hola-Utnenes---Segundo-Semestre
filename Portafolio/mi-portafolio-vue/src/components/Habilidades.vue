<script setup>
defineOptions({ name: 'HabilidadesSection' })
import { ref } from 'vue'

const habilidades = ref([
  { id: 1, nombre: 'Java', claseIcono: 'fab fa-java', claseBarra: 'java' },
  { id: 2, nombre: 'Python', claseIcono: 'fab fa-python', claseBarra: 'python' },
  { id: 3, nombre: 'JavaScript', claseIcono: 'fab fa-js-square', claseBarra: 'js' },
  { id: 4, nombre: 'CSS', claseIcono: 'fab fa-css3-alt', claseBarra: 'css' },
  { id: 5, nombre: 'GitHub', claseIcono: 'fab fa-github', claseBarra: 'github' }
])
</script>

<template>
  <section id="habilidades">
    <h2>Habilidades Técnicas</h2>
    <div class="habilidades-container">
      <div v-for="habilidad in habilidades" :key="habilidad.id" class="habilidad">
        <i :class="habilidad.claseIcono" aria-hidden="true"></i>
        <span>{{ habilidad.nombre }}</span>
        <div class="barra">
          <div :class="'barra-progreso ' + habilidad.claseBarra"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>
