<script setup>
import { ref } from "vue";

const fechaColor = ref([
  { color: "#41516c" },
  { color: "#e24a68" },
  { color: "#452452" },
  { color: "#41c49c" },
]);

const educacion = ref([
  {
    fecha: "2024",
    titulo: "Técnico en Industrias de Proceso",
    descripcion:
      "Cursado en escuela Manuel Nicolás Savio, 6 años completos recurridos a la química y la industria.",
  },
  {
    fecha: "2025 - Actualidad",
    titulo: "Técnico en Programación",
    descripcion:
      "Actualmente cursando para técnico en programación, adquiriendo nuevos conocimientos y aprendiendo a resolver retos como uno de los líderes de 'Hola Utnenes' en la cohorte 2025 de la UTN San Rafael.",
    enlace: "https://www.google.com.ar",
  },
]);
</script>

<template>
  <div class="timeline-container">
    <h2 class="titulo-principal">Mi Educación</h2>
    <ul>
      <li
        v-for="(item, index) in educacion"
        :key="index"
        :style="{ '--fecha-color': fechaColor[index].color }"
        class="tarjeta"
      >
        <div class="fecha">{{ item.fecha }}</div>
        <h3 class="titulo">{{ item.titulo }}</h3>
        <p class="descripcion">{{ item.descripcion }}</p>
        <a
          v-if="item.enlace"
          :href="item.enlace"
          target="_blank"
          class="enlace"
        >
          Saber más →
        </a>
      </li>
    </ul>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");

body {
  font-family: "Poppins", sans-serif;
  background: linear-gradient(135deg, #1c1f26, #2e3545);
  color: #f0f0f0;
  margin: 0;
  padding: 0;
}

.timeline-container {
  width: min(800px, 90%);
  margin: 4rem auto;
  text-align: center;
}

.titulo-principal {
  font-size: 2rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 2rem;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

ul {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 0;
  list-style: none;
}

.tarjeta {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 2rem;
  text-align: left;
  border-left: 6px solid var(--fecha-color);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.tarjeta:hover {
  transform: translateY(-6px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
}

.fecha {
  font-weight: 600;
  color: var(--fecha-color);
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.titulo {
  font-size: 1.5rem;
  color: #fff;
  margin-bottom: 0.5rem;
}

.descripcion {
  font-weight: 300;
  color: #dcdcdc;
  line-height: 1.6;
}

.enlace {
  display: inline-block;
  margin-top: 1rem;
  font-weight: 500;
  color: var(--fecha-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

.enlace:hover {
  color: #fff;
  text-decoration: underline;
}

@media (max-width: 600px) {
  .tarjeta {
    padding: 1.5rem;
  }
  .titulo-principal {
    font-size: 1.6rem;
  }
}
</style>
