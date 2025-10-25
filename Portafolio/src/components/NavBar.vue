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
  color: red;
}

/* Los enlaces (<a>) suelen tener una regla global 'a { color: ... }' que tiene
   prioridad sobre el color heredado del contenedor. Para que los enlaces dentro
   de la navbar se vean con el color deseado, dirigimos la regla a los items o
   a los enlaces dentro de .navbar. */
.navbar .navbar-item,
.navbar {
  background-color: var(--vt-c-indigo);
  color: #fff;
  padding: 0.5rem 1rem;
  align-items: center;
}
.navbar-items {
  color: #fff;
  text-decoration: none;
  margin-right: 1rem;
}
.navbar-menu {
  display: flex;
  justify-content: flex-end;
}
.navbar-list {
  list-style: none;
}
</style>
