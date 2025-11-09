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
    fecha: "2025",
    titulo: "Primer Semestre",
    descripcion:
      "Se cursan materias como: Fundamentos en programacion, Programacion I (Java, Javascript , Python , Github ), Matematica, Arquietctura de S.O. , Organizacion Empresarial",
    enlace: "www.google.com.ar",
  },
  {
    fecha: "2025",
    titulo: "Segundo Semestre",
    descripcion:
      "Se cursan materias como:Programacion II (Java, Javascript , Python , Github, Vue ), Estadistica , Bases De Datos, Ingles",
    enlace: "www.google.com.ar",
  },
    {  fecha: "2026",
    titulo: "Tercer Semestre",
    descripcion:
      "Esperando por mas materias espectaculares ....",
    enlace: "www.google.com.ar",}
,
      {fecha: "2026",
    titulo: "Cuarto Semestre",
    descripcion:
      "Esperando por mas materias espectaculares ....",
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
  --color: rgba(30, 30, 30);
  --bgcolor: rgba(245, 245, 245);
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
  background: rgb(225, 225, 225);
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
  background-color: var(--fecha-color);
  color: white;
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
  aspect-ratio: 1;
  background: var(--fecha-color);
  background-image: linear-gradient(rgba(0, 0, 0, 0.2) 100%, transparent);
  position: absolute;
  top: 100%;
  clip-path: polygon(0 0, 100% 0, 0 100%);
  right: 0;
}

ul li .fecha::after {
  content: "";
  position: absolute;
  width: 1rem;
  aspect-ratio: 1;
  background: var(--bgcolor);
  border: 0.3rem solid var(--fecha-color);
  border-radius: 50%;
  top: 50%;
  transform: translate(50%, -50%);
  right: calc(100% + var(--col-gap) + var(--line-w) / 2);
}

ul li .title,
ul li .descripcion {
  background: var(--bgcolor);
  position: relative;
  padding-inline: 1.5rem;
}

ul li .title {
  overflow: hidden;
  padding-block-start: 1.5rem;
  padding-block-end: 1rem;
  font-weight: 500;
}

ul li .descripcion {
  padding-block-end: 1.5rem;
  font-weight: 300;
}

ul li .title::before,
ul li .descripcion::before {
  content: "";
  position: absolute;
  width: 90%;
  height: 0.5rem;
  background: rgba(0, 0, 0, 0.5);
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
    transform: scale(-1);
  }

  ul li:nth-child(odd) .fecha::after {
    transform: translate(-50%, -50%);
    left: calc(100% + var(--col-gap) + var(--line-w) / 2);
    right: auto;
  }
}

.credits {
  margin-top: 1rem;
  text-align: center;
}

.credits a {
  color: var(--color);
}
</style>
