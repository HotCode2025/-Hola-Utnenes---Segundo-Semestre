<script setup>
defineOptions({ name: 'SiteFooter' })
</script>

<template>
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <h3>Serena Olmedo</h3>
        <p class="small">Técnico en Programación</p>
      </div>

      <div class="footer-links">
        <a href="#sobremi">Sobre Mí</a>
        <a href="#estudios">Estudios</a>
        <a href="#experiencia">Experiencia</a>
        <a href="#habilidades">Habilidades</a>
        <a href="#proyectos">Proyectos</a>
        <a href="#contacto">Contacto</a>
      </div>

      <div class="footer-social">
        <a href="https://github.com/sereolm" target="_blank" rel="noopener" aria-label="GitHub">GitHub</a>
        <a href="https://linkedin.com/in/serena-del-valle-olmedo" target="_blank" rel="noopener" aria-label="LinkedIn">LinkedIn</a>
        <a href="mailto:serenadelvalle25@gmail.com" aria-label="Email">Email</a>
      </div>
    </div>
    <div class="footer-copy">&copy; 2025 - Portafolio creado por Serena Olmedo</div>
  </footer>
</template>

<style scoped>
.site-footer{
  background: rgba(0,0,0,0.7);
  color: #ddd;
  padding: 1.6rem 1rem;
  margin-top: 2rem;
}
.footer-inner{
  display:flex;
  flex-wrap:wrap;
  gap:1rem;
  align-items:center;
  justify-content:space-between;
  max-width:1000px;
  margin:0 auto 0.6rem auto;
}
.footer-brand h3{margin:0 0 0.2rem 0;color:#fff}
.footer-links a,
.footer-social a{color:#cfcbe0;text-decoration:none;margin-right:0.8rem;font-size:0.95rem}
.footer-links a:hover,.footer-social a:hover{color:#fff}
.footer-copy{ text-align:center; font-size:0.85rem; color:#bbb }
@media(max-width:600px){
  .footer-inner{ flex-direction:column; align-items:center }
  .footer-links{ text-align:center }
}
</style>
