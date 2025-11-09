<script setup>
import { ref } from 'vue';
import img1 from '/src/components/icons/js.svg';
import img2 from '/src/components/icons/python.svg';
import img3 from '/src/components/icons/html-css.svg';
import img4 from '/src/components/icons/java.svg';
import img5 from '/src/components/icons/swift.svg';
import img6 from '/src/components/icons/react.svg';
import img7 from '/src/components/icons/vue.svg';
import img11 from '/src/components/icons/git.svg';
import img15 from '/src/components/icons/visual.svg';
import img19 from '/src/components/icons/arg.svg';
import img20 from '/src/components/icons/eeuu.svg';

const habilidades = ref([
  { id: 1, nombre: 'Lenguajes de Programación', habilidades: [
      { id: 1, nombre: 'JavaScript', nivel: 'Intermedio', icono: img1 },
      { id: 2, nombre: 'Python', nivel: 'Básico', icono: img2 },
      { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: img3 },
      { id: 4, nombre: 'Java', nivel: 'Básico', icono: img4 },
      { id: 5, nombre: 'Swift', nivel: 'Intermedio', icono: img5 },
    ] },
  { id: 2, nombre: 'Frameworks y Librerías', habilidades: [
      { id: 1, nombre: 'React.js', nivel: 'Intermedio', icono: img6 },
      { id: 2, nombre: 'Vue.js', nivel: 'Básico', icono: img7 },
    ] },
  { id: 3, nombre: 'Herramientas y Software', habilidades: [
      { id: 1, nombre: 'Git', nivel: 'Intermedio', icono: img11 },
      { id: 2, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: img15 },
    ] },
  { id: 4, nombre: 'Idiomas', habilidades: [
      { id: 1, nombre: 'Español', nivel: 'Nativo', icono: img19 },
      { id: 2, nombre: 'Inglés', nivel: 'Intermedio (B2)', icono: img20 },
    ] },
]);
</script>

<template>
  <div class="skills-contenedor">
    <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
      <h3>{{ habilidad.nombre }}</h3>
      <ul class="skills">
        <li v-for="h in habilidad.habilidades" :key="h.id" class="skill">
          <img :src="h.icono" :alt="h.nombre" />
          <span>{{ h.nombre }}: {{ h.nivel }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>


<style scoped>
.skills-contenedor {
  padding: 2rem;
  background-color: var(--color-bg-card);
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(255, 213, 79, 0.1);
}
.skills-categoria h3 {
  color: var(--color-accent);
  margin-bottom: 10px;
}
.skills {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}
.skill {
  background-color: #111;
  border: 1px solid var(--color-border);
  border-left: 4px solid var(--color-accent);
  border-radius: 8px;
  padding: 0.7rem 1rem;
  display: flex;
  align-items: center;
  gap: 10px;
  width: 220px;
  transition: 0.3s;
}
.skill:hover {
  background-color: var(--color-accent);
  color: #000;
  transform: scale(1.05);
}
.skill img { width: 30px; }
.skill span { font-weight: 500; }
</style>
