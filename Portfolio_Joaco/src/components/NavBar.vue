<template>
  <nav class="navbar">
    <div class="navbar-container">
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
  { id: 1, nombre: "EDUCACIÓN", enlace: "#educacion" },
  { id: 2, nombre: "EXPERIENCIA", enlace: "#experiencia" },
  { id: 3, nombre: "PROYECTOS", enlace: "#proyectos" },
  { id: 4, nombre: "HABILIDADES", enlace: "#habilidades" },
  { id: 5, nombre: "INTERESES", enlace: "#intereses" },
]);
</script>

<style scoped>
.navbar {
  background-color: var(--color-background-soft);
  border-bottom: 1px solid var(--color-border);
  padding: 1rem 2rem;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  backdrop-filter: blur(10px);
  transition: all var(--transition-smooth);
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
}

.navbar-list {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 1.5rem;
  justify-content: center;
}

.navbar-item {
  color: var(--color-text);
  text-decoration: none;
  font-weight: 600;
  padding: 0.75rem 1.25rem;
  border-radius: var(--border-radius);
  transition: all var(--transition-smooth);
  position: relative;
  text-transform: uppercase;
  font-size: 0.9rem;
  letter-spacing: 0.5px;
}

.navbar-item::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #a78bfa, #60a5fa);
  transition: all var(--transition-smooth);
  transform: translateX(-50%);
  border-radius: 2px;
}

.navbar-item:hover {
  color: #a78bfa;
  background-color: rgba(147, 197, 253, 0.1);
}

.navbar-item:hover::before {
  width: 80%;
}

.navbar-item:active {
  transform: translateY(1px);
}

/* Estado activo para la sección actual */
.navbar-item.active {
  color: #a78bfa;
  background-color: rgba(147, 197, 253, 0.15);
}

.navbar-item.active::before {
  width: 80%;
}

@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
  }
  
  .navbar-list {
    gap: 0.5rem;
    flex-wrap: wrap;
  }
  
  .navbar-item {
    padding: 0.5rem 1rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .navbar-list {
    flex-direction: column;
    align-items: center;
    width: 100%;
    gap: 0.25rem;
  }
  
  .navbar-item {
    width: 100%;
    text-align: center;
    margin: 0.1rem 0;
  }
}
</style>
