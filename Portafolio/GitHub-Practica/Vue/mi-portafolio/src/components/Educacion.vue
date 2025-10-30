<script setup>
import { ref } from 'vue'

// Datos de la línea de tiempo
const cursos = ref([
  {
    id: 1,
    fecha: '2024',
    titulo: 'Tecnicatura Universitaria en Programación',
    descripcion: 'Formación orientada al desarrollo de software, lógica de programación y bases de datos.',
    enlace: 'https://www.utn.edu.ar'
  },
  {
    id: 2,
    fecha: '2023',
    titulo: 'Curso de Redes Informáticas',
    descripcion: 'Aprendizaje de cableado estructurado, configuración de routers y protocolos TCP/IP.',
    enlace: 'https://www.cisco.com'
  },
  {
    id: 3,
    fecha: '2022',
    titulo: 'Curso de Instalador Técnico',
    descripcion: 'Introducción a la instalación de sistemas eléctricos y mantenimiento preventivo.',
    enlace: '#'
  }
])
</script>

<template>
  <section id="educacion">
    <h2>Educación - Cursos</h2>
    <ul class="timeline">
      <li v-for="curso in cursos" :key="curso.id">
        <div class="fecha">{{ curso.fecha }}</div>
        <div class="titulo">{{ curso.titulo }}</div>
        <div class="descripcion">{{ curso.descripcion }}</div>
        <a class="enlace" :href="curso.enlace" target="_blank">Ver más</a>
      </li>
    </ul>
  </section>
</template>

<style scoped>
h2 {
  color: #42b883;
  text-align: left;
  margin-bottom: 1rem;
}

.timeline {
  border-left: 3px solid #35495e;
  margin-left: 2rem;
  padding-left: 1rem;
}

.timeline li {
  list-style: none;
  margin-bottom: 2rem;
  position: relative;
}

.timeline li::before {
  content: "●";
  color: #42b883;
  position: absolute;
  left: -1.2rem;
  top: 0;
  font-size: 1.2rem;
}

.fecha {
  font-weight: bold;
  background-color: #f9f9f9;
  border-bottom: 2px solid #42b883;
  padding: 0.3rem 0.5rem;
}

.titulo {
  font-weight: bold;
  margin-top: 0.5rem;
  text-align: center;
}

.descripcion {
  padding: 0.5rem;
  color: #333;
}

.enlace {
  display: block;
  text-align: center;
  color: #42b883;
  text-decoration: none;
  font-weight: bold;
  margin-top: 0.3rem;
}

.enlace:hover {
  text-decoration: underline;
}
</style>
