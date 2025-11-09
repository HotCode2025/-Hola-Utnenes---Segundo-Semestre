<template>
  <nav class="navbar">
    <div class="navbar-menu">
      <ul class="navbar-list">
        <li v-for="nav in navegacion" :key="nav.id">
          <a :href="nav.enlace" class="navbar-item">{{ nav.nombre }}</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";
const navegacion = ref([
  { id: 1, nombre: "EDUCACION", enlace: "#educacion" },
  { id: 2, nombre: "EXPERIENCIA", enlace: "#experiencia" },
  { id: 3, nombre: "PROYECTOS", enlace: "#proyectos" },
  { id: 4, nombre: "HABILIDADES", enlace: "#habilidades" },
  { id: 5, nombre: "INTERESES", enlace: "#intereses" },
]);
</script>

<style scoped>
.navbar {
  background-color: #2c3e50;
  color: #fff;
  padding: 1rem;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.navbar-menu {
  display: flex;
  justify-content: flex-end;
  max-width: 1200px;
  margin: 0 auto;
}

.navbar-list {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 1rem;
}

.navbar-item {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: all 0.3s ease;
  border: 1px solid transparent;
}

.navbar-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.2);
}

@media (max-width: 768px) {
  .navbar-list {
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .navbar-menu {
    justify-content: center;
  }

  .navbar-item {
    width: 100%;
    text-align: center;
    margin: 0.25rem 0;
  }
}
</style>
