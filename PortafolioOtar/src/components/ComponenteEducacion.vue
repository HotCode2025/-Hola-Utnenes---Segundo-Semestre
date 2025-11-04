<script setup>
import { ref } from "vue";
const fechaColor = ref([]);
fechaColor.value = [
    { color: "#41516c" },
    { color: "#e24a68" },
    { color: "#452452" },
    { color: "#41c49c" },
];
const educacion = ref([]);
educacion.value = [
  {
    fecha: "2011 - Actualidad",
    titulo: "Tecnico Superior en Gastronomia",
    descripcion:
      "Egresado de Chef , Adquiriendo conocimientos siempre, y manteniendome al dia con las mejores practicas y tecnicas culinarias",
    enlace: "www.google.com.ar",
  },
  {
    fecha: "2021-2022",
    titulo: "Fullstack Js - Coderhouse",
    descripcion:
      "Cursado de desarrollador fullstack en js (stack MERN).",
    enlace: "www.google.com.ar",
  },
    {  fecha: "2025 - Actualidad",
    titulo: "Tecnico en Programacion",
    descripcion:
      "Actualmente cursando para tecnico en programacion, adquiriendo nuevos conocimientos, y aprendiendo y aportando en los retos y tareas que se van presentando en el camino como uno de los lideredes de ('Hola Utnenes') de la cohorte 2025 de la UTN SAN RAFAEL",
    enlace: "www.google.com.ar",}
,

];
</script>

<template>
  <div>
    <ul>
      <li
        v-for="(item, index) in educacion"
        :key="index"
        :style="{ '--fecha-color': fechaColor[index].color }"
      >
        <div class="fecha">{{ item.fecha }}</div>
        <h3 class="title">{{ item.titulo }}</h3>
        <div class="descripcion">{{ item.descripcion }}</div>
        <a :href="item.enlace" class="enlace">Saber Mas...</a>
      </li>
    </ul>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?Family=Poppins:wght@300;500;700&display=swap");

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  --color: var(--color-text);
  --bgcolor: var(--color-background);
  min-height: 100vh;
  display: grid;
  align-items: center;
  gap: 2rem;
  font-family: "Poppins", sans-serif;
  color: var(--color);
  background-color: var(--bgcolor);
}

ul {
  --col-gap: 2rem;
  --row-gap: 2rem;
  --line-w: 0.25rem;
  display: grid;
  grid-template-columns: var(--line-w) 1fr;
  grid-auto-columns: max-content;
  column-gap: var(--col-gap);
  list-style: none;
  width: min(60rem, 90%);
  margin-inline: auto;
  margin-top: 2rem;
}

ul::before {
  content: "";
  grid-column: 1;
  grid-row: 1 / span 20;
  background: var(--color-border);
  border-radius: calc(var(--line-w) / 2);
}

ul li:not(:last-child) {
  margin-bottom: var(--row-gap);
}

ul li {
  grid-column: 2;
  --inlinerP: 1.5rem;
  margin-inline: var(--inlinerP);
  grid-row: span 2;
  display: grid;
  grid-template-rows: min-content min-content min-content;
}

ul li .fecha {
  --dateH: 3rem;
  height: var(--dateH);
  margin-inline: calc(var(--inlinerP) * -1);
  text-align: center;
  background-color: var(--color-primary);
  color: var(--color-background);
  font-size: 1.25rem;
  font-weight: 700;
  display: grid;
  place-content: center;
  position: relative;
  border-radius: calc(var(--dateH) / 2) 0 0 calc(var(--dateH) / 2);
}

ul li .fecha::before {
  content: "";
  width: var(--inlinerP);
  height: var(--inlinerP);
  background: var(--color-primary);
  position: absolute;
  top: 100%;
  clip-path: polygon(0 0, 100% 0, 0 100%);
  right: 0;
}

ul li .fecha::after {
  content: "";
  position: absolute;
  width: 1rem;
  height: 1rem;
  background: var(--color-background);
  border: 0.3rem solid var(--color-primary);
  border-radius: 50%;
  top: 50%;
  transform: translate(50%, -50%);
  right: calc(100% + var(--col-gap) + var(--line-w) / 2);
}

ul li .title,
ul li .descripcion {
  background: var(--color-background-soft);
  position: relative;
  padding-inline: 1.5rem;
}

ul li .title {
  overflow: hidden;
  padding-block-start: 1.5rem;
  padding-block-end: 1rem;
  font-weight: 500;
  color: var(--color-heading);
}

ul li .descripcion {
  padding-block-end: 1.5rem;
  font-weight: 300;
  color: var(--color-text);
}

ul li .title::before,
ul li .descripcion::before {
  content: "";
  position: absolute;
  width: 90%;
  height: 0.5rem;
  background: var(--color-border);
  left: 50%;
  border-radius: 50%;
  filter: blur(4px);
  transform: translate(-50%, 50%);
}

ul li .title::before {
  bottom: calc(100% + 0.125rem);
}

ul li .descripcion::before {
  z-index: -1;
  bottom: 0.25rem;
}


@media (min-width: 40rem) {
  ul {
    grid-template-columns: 1fr var(--line-w) 1fr;
  }

  ul::before {
    grid-column: 2;
  }

  ul li:nth-child(odd) {
    grid-column: 1;
  }

  ul li:nth-child(even) {
    grid-column: 3;
  }

  ul li:nth-child(2) {
    grid-row: 2/4;
  }


  ul li:nth-child(odd) .fecha {
    border-radius: 0 calc(var(--dateH) / 2) calc(var(--dateH) / 2) 0;
  }


  ul li:nth-child(odd) .fecha::before {
    left: 0;
    right: auto;
    clip-path: polygon(100% 0, 100% 100%, 0 0);
  }


  ul li:nth-child(odd) .fecha::after {
    left: calc(100% + var(--col-gap) + var(--line-w) / 2);
    right: auto;
    transform: translate(-50%, -50%);
  }
}

.credits {
  margin-top: 1rem;
  text-align: center;
}

.credits a {
  color: var(--color-primary);
}

.credits a:hover {
  color: var(--color-hover);
}
</style>