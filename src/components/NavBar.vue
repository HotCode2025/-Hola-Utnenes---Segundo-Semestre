<template>
  <nav class="navbar">
    <div class="navbar-container">
      <ul class="navbar-list">
        <li v-for="nav in navegacion" :key="nav.id">
          <a :href="nav.enlace" 
           class="navbar-item">{{ nav.nombre }}</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";

const navegacion = ref([
  { id: 1, nombre: "EDUCACIÓN", enlace: "#educacion" },
  { id: 2, nombre: "EXPERIENCIA", enlace: "#experiencia" },
  { id: 3, nombre: "PROYECTOS", enlace: "#proyectos" },
  { id: 4, nombre: "HABILIDADES", enlace: "#habilidades" },
  { id: 5, nombre: "INTERESES", enlace: "#intereses" },
]);
</script>

<style>
/* Estilos Globales (aplicados a todo el body) */
body {
  margin: 0;
  /* El fondo de la página debe ser negro para que todo el diseño funcione */
  background-color: #000; 
  color: #fff; 
  font-family: sans-serif;
}

#app {
  /* Contenedor principal de Vue */
  min-height: 100vh;
}
</style>


<style scoped>
.navbar {
  background: linear-gradient(to right, #fff8f0, #ffe4e1); /* blanco cálido a rosa claro */
  padding: 1rem 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  border-bottom: 2px solid #fffacd; /* amarillo claro */
}

.navbar-container {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
}

.navbar-list {
  list-style: none;
  display: flex;
  gap: 2rem;
  padding: 0;
  margin: 0;
}

.navbar-item {
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1rem;
  color: #ff69b4; /* rosa fuerte */
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.navbar-item:hover {
  background-color: #fffacd; /* amarillo claro */
  color: #4a4a4a;
  transform: scale(1.05);
}
</style>