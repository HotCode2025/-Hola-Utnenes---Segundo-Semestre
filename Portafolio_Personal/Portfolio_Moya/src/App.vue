<script setup>
import HeaderPortfolio from "./components/HeaderPortfolio.vue";
import SobreMi from "./components/SobreMi.vue";
import Proyectos from "./components/MisProyectos.vue";
import Tecnologias from "./components/MisTecnologias.vue";
import Contacto from "./components/MiContacto.vue";
import FooterPortfolio from "./components/FooterPortfolio.vue";
import ScrollProgress from "./components/ScrollProgress.vue";

</script>

<template>
  <div>
    <ScrollProgress />

    <HeaderPortfolio />

    <main>
      <SobreMi />
      <Proyectos />
      <Tecnologias />
      <Contacto />
    </main>

    <FooterPortfolio />
  </div>
</template>


<style>
body {
  margin: 0;
  font-family: "Segoe UI", sans-serif;
  background-color: #111;
  color: #fff;
}

/* Encabezado del sitio */
header {
  background-color: #000;
  padding: 40px 20px;
  text-align: center;
}

/* Imagen de perfil circular moderna */
.foto-perfil {
  width: 160px;
  height: 160px;
  object-fit: cover;
  border-radius: 50%;
  border: 3px solid #ff8000;
  box-shadow: 0 4px 10px rgba(255, 128, 0, 0.2);
  margin-bottom: 20px;
}

h1 {
  margin: 10px 0;
  color: orange;
}

/* Menú de navegación */
nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 15px;
  font-weight: bold;
}

nav a:hover {
  color: orange;
}

/* Cuerpo principal del sitio */
main {
  max-width: 800px;
  margin: auto;
  padding: 40px 20px;
}

section {
  margin-bottom: 50px;
}

h2 {
  color: orange;
  border-bottom: 2px solid orange;
  padding-bottom: 5px;
}

ul {
  list-style: none;
  padding-left: 0;
}

ul li {
  margin-bottom: 20px;
}

ul li::before {
  content: "🔸 ";
  color: orange;
}

footer {
  background-color: #000;
  text-align: center;
  padding: 20px;
  color: #888;
}

a {
  color: orange;
}

a:hover {
  text-decoration: underline;
}
</style>
