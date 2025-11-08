<script setup>
const educacion = {
  titulo: "Bachillerato en Economía",
  institucion: "San Juan Bosco - S203",
  año: "2019"
};
</script>

<template>
  <section class="edu">
    <h2>Educación</h2>
    <div class="item">
      <h3>{{ educacion.titulo }}</h3>
      <p>{{ educacion.institucion }} - {{ educacion.año }}</p>
    </div>
  </section>
</template>

<style scoped>
.edu {
  padding: 2rem;
  background: #e6f0ff;
  border-radius: 12px;
  margin: 1rem;
}

h2 {
  color: #1a73e8;
  text-align: center;
  margin-bottom: 1.5rem;
}

h3 {
  color: #0a2a43;
}

p {
  color: #184e77;
}
</style>
