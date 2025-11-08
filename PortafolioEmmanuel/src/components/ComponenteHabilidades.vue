<script setup>
const habilidades = {
  lenguajes: ["HTML", "CSS", "Python"],
  herramientas: ["Git", "GitHub", "VS Code"],
  idiomas: ["Español"]
};
</script>

<template>
  <section class="fade-up">
    <h2>Habilidades</h2>

    <div class="categoria">
      <h3>Lenguajes de Programación</h3>
      <ul>
        <li v-for="l in habilidades.lenguajes" :key="l">{{ l }}</li>
      </ul>
    </div>

    <div class="categoria">
      <h3>Herramientas y Software</h3>
      <ul>
        <li v-for="h in habilidades.herramientas" :key="h">{{ h }}</li>
      </ul>
    </div>

    <div class="categoria">
      <h3>Idiomas</h3>
      <ul>
        <li v-for="i in habilidades.idiomas" :key="i">{{ i }}</li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
h2 {
  text-align: center;
  margin-bottom: 1.5rem;
}
.categoria {
  margin-bottom: 1.5rem;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  display: inline-block;
  background: #e6f0ff;
  color: #0a2a43;
  padding: 0.4rem 0.8rem;
  border-radius: 8px;
  margin: 0.3rem;
  transition: transform 0.2s ease;
}
li:hover {
  transform: scale(1.05);
  background: #cbe3ff;
}
</style>