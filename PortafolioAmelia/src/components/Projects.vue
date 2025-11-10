<template>
  <section class="projects" data-aos="fade-up">
    <h2>Proyectos</h2>
    <div class="project-list">
      <div class="project-card" v-for="(project, index) in projects" :key="index" data-aos="zoom-in">
        <h3>{{ project.name }}</h3>
        <p>{{ project.description }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
const projects = [
  { name: 'Proyecto 1', description: 'Descripción breve del proyecto 1' },
  { name: 'Proyecto 2', description: 'Descripción breve del proyecto 2' },
  { name: 'Proyecto 3', description: 'Descripción breve del proyecto 3' },
]
</script>

<style scoped>
/* Estilos de Projects */
</style>