<script setup>
import { ref } from 'vue'
const navegacion = ref([
  { id: 1, nombre: 'Educación', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  {id: 4, nombre: 'Intereses', enlace: '#intereses' }
])
</script>

<template>
  <nav class="navbar">
    <ul>
      <li v-for="nav in navegacion" :key="nav.id">
        <a :href="nav.enlace">{{ nav.nombre }}</a>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: #000;
  border-bottom: 2px solid var(--color-accent);
  padding: 1rem 0;
  text-align: center;
}
ul {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}
a {
  color: var(--color-text-light);
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 1px;
}
a:hover { color: var(--color-accent); }
</style>
