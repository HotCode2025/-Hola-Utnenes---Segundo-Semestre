<script setup>
import { ref } from 'vue';
const titulo = 'Asesor comercial y de logistica';
const fecha = 'Desde Febrero 2019 / Actualidad';
const experiencias = ref([
  { id: 1, parrafo: 'Gestión integral de clientes, administración de stock y coordinación de logística.' },
  { id: 2, parrafo: 'Diseñé y desarrollé aplicaciones web utilizando Node.js, React y MongoDB, logrando reducir el tiempo de carga de las páginas en un 50%.' },
  { id: 3, parrafo: 'Desarrollo de estrategias de fidelización y resolución de incidencias.' },
  { id: 4, parrafo: 'Implementación de procesos de autogestión y optimización del tiempo de atención.' },
  
]);
</script>

<template>
  <div class="card">
    <h3 class="titulo">{{ titulo.toLocaleUpperCase() }}</h3>
    <p class="fecha">{{ fecha }}</p>
    <ul class="listado">
      <li class="item" v-for="experencia in experiencias" :key="experencia.id">
        <p>{{ experencia.parrafo }}</p>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.card {
  background-color: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-left: 5px solid var(--color-accent);
  border-radius: 10px;
  padding: 2rem;
  box-shadow: 0 0 20px rgba(255, 213, 79, 0.15);
  transition: 0.3s;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0 25px rgba(255, 213, 79, 0.3);
}
.titulo {
  color: var(--color-accent);
  text-align: center;
  margin-bottom: 0.5rem;
}
.fecha {
  color: #ccc;
  text-align: center;
  margin-bottom: 1rem;
  font-style: italic;
}
.listado {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  background-color: #111;
  border-radius: 8px;
  padding: 1rem;
  border: 1px solid var(--color-border);
  transition: 0.3s;
}
.item:hover {
  background-color: #222;
  border-color: var(--color-accent);
}
.item p {
  color: var(--color-text-light);
}
</style>
