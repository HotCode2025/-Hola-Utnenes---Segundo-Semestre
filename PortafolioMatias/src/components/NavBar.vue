<script setup>
import { ref } from 'vue'

const navegacion = ref([
  { id: 1, nombre: 'Educación', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  { id: 5, nombre: 'Intereses', enlace: '#intereses' }
])

// Estado del menú hamburguesa
const menuAbierto = ref(false)
const alternarMenu = () => {
  menuAbierto.value = !menuAbierto.value
}
</script>

<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <a href="#">Mi Portafolio</a>
    </div>

    <!-- Botón hamburguesa (solo visible en pantallas chicas) -->
    <button class="menu-toggle" @click="alternarMenu">
      ☰
    </button>

    <ul :class="['nav-list', { activo: menuAbierto }]">
      <li v-for="nav in navegacion" :key="nav.id">
        <a :href="nav.enlace" class="navbar-item" @click="menuAbierto = false">
          {{ nav.nombre }}
        </a>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  background: #35495e;
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: .75rem 1.25rem;
}
.navbar-logo a {
  color: #fff;
  font-weight: bold;
  text-decoration: none;
  font-size: 1.1rem;
}
.nav-list {
  display: flex;
  gap: 1rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.navbar-item {
  color: #fff;
  text-decoration: none;
  transition: 0.3s;
}
.navbar-item:hover {
  color: #42b883;
}

/* menú hamburguesa */
.menu-toggle {
  background: none;
  border: none;
  color: #fff;
  font-size: 1.5rem;
  cursor: pointer;
  display: none;
}

/* vista móvil */
@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }
  .nav-list {
    position: absolute;
    top: 60px;
    right: 0;
    background: #35495e;
    flex-direction: column;
    width: 200px;
    transform: translateX(100%);
    transition: transform 0.3s ease;
  }
  .nav-list.activo {
    transform: translateX(0);
  }
  .nav-list li {
    padding: 1rem;
    border-bottom: 1px solid rgba(255,255,255,0.1);
  }
}
</style>

