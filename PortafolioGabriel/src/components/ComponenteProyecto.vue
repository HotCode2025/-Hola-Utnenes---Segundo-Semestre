<script setup>
    import { ref } from 'vue'

    // 🔧 IMPORTÁ TUS IMÁGENES (colocalas en src/assets/proyectos/)
    const imgPayunia = new URL('../assets/proyectos/payunia.jpg', import.meta.url).href
    const imgAstroturismo = new URL('../assets/proyectos/astroturismo.jpg', import.meta.url).href
    const imgMalacara = new URL('../assets/proyectos/malacara.jpg', import.meta.url).href
    const imgLasLenas = new URL('../assets/proyectos/laslenas.jpg', import.meta.url).href
    const imgWinForms = new URL('../assets/proyectos/winforms_sistema_socios.png', import.meta.url).href
    const imgPortfolio = new URL('../assets/proyectos/portfolio_vue.jpg', import.meta.url).href

    const proyectos = ref([
        {
            id: '1',
            titulo: 'Payunia Travel – Payunia Total',
            descripcion: 'Sitio con info y reservas de excursión Payunia Total (Elementor, calendario externo, fotos).',
            linkPagina: 'https://www.payuniatravel.tur.ar/payunia',
            linkGithub: '',
            img: imgPayunia
        },
        {
            id: '2',
            titulo: 'Astroturismo Malargüe',
            descripcion: 'Experiencia de observación astronómica: reconocimiento del cielo, telescopios y astrofotografía.',
            linkPagina: 'https://gabrielmoya.pixieset.com/muestraastroturismo/', // Galería pública
            linkGithub: '',
            img: imgAstroturismo
        },
        {
            id: '3',
            titulo: 'Excursión Volcán Malacara',
            descripcion: 'Circuito Malacara + Antena DS3 de la ESA. Logística, guías y reservas.',
            linkPagina: '', // si tenés landing específica, pegala acá
            linkGithub: '',
            img: imgMalacara
        },
        {
            id: '4',
            titulo: 'Traslado a Las Leñas',
            descripcion: 'Servicio de transporte desde Malargüe con beneficios para alquiler de equipos.',
            linkPagina: '',
            linkGithub: '',
            img: imgLasLenas
        },
        {
            id: '5',
            titulo: 'Final C# WinForms – Gestión de Socios',
            descripcion: 'App de escritorio con Access (BD_Clientes.mdb): ABM, listados e impresión personalizada.',
            linkPagina: '',
            linkGithub: '', // si lo subís a GitHub, pegá el repo
            img: imgWinForms
        },
        {
            id: '6',
            titulo: 'Portfolio Personal (Vue 3)',
            descripcion: 'Sitio personal en Vue (CDN/Vite). Componentes, secciones y estilos propios.',
            linkPagina: '', // cuando lo subas (GitHub Pages/Netlify), pegá el link
            linkGithub: '',
            img: imgPortfolio
        }
    ])
</script>

<template>
    <div class="galeria">
        <div class="proyecto" v-for="p in proyectos" :key="p.id">
            <div class="proyecto-img-container">
                <img :src="p.img" :alt="p.titulo" />
                <div class="proyecto-overlay"></div>
            </div>
            <div class="proyecto-info">
                <h3>{{ p.titulo }}</h3>
                <p>{{ p.descripcion }}</p>

                <div class="proyecto-links">
                    <a v-if="p.linkPagina"
                       class="btn-ver-mas"
                       :href="p.linkPagina"
                       target="_blank"
                       rel="noopener">Ver sitio</a>

                    <a v-if="p.linkGithub"
                       class="github-link"
                       :href="p.linkGithub"
                       target="_blank"
                       rel="noopener"
                       aria-label="Repositorio en GitHub">
                        <svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24">
                            <path d="M12 .5a12 12 0 0 0-3.79 23.4c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.41-1.35-1.79-1.35-1.79-1.1-.75.08-.74.08-.74 1.21.09 1.85 1.25 1.85 1.25 1.08 1.85 2.83 1.31 3.52 1 .11-.78.42-1.31.76-1.61-2.66-.3-5.46-1.33-5.46-5.93 0-1.31.47-2.38 1.24-3.22-.13-.31-.54-1.56.12-3.25 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.66 1.69.25 2.94.12 3.25.77.84 1.24 1.91 1.24 3.22 0 4.61-2.8 5.62-5.47 5.92.43.37.81 1.09.81 2.21v3.28c0 .32.22.7.83.58A12 12 0 0 0 12 .5z" />
                        </svg>
                        GitHub
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .galeria {
        width: 100%;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        padding: 2rem;
        background: var(--color-background);
    }

    .proyecto {
        display: flex;
        flex-direction: column;
        border: 1px solid var(--color-border);
        border-radius: var(--border-radius-lg);
        overflow: hidden;
        background: var(--color-background-soft);
        transition: all var(--transition-smooth);
        position: relative;
    }

        .proyecto:hover {
            transform: translateY(-5px);
            border-color: var(--color-primary);
            box-shadow: var(--shadow-glow);
        }

    .proyecto-img-container {
        position: relative;
        overflow: hidden;
        height: 200px;
    }

    .proyecto img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform var(--transition-smooth);
    }

    .proyecto:hover img {
        transform: scale(1.05);
    }

    .proyecto-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(to bottom, transparent 0%, var(--color-background) 100%);
        opacity: 0.3;
        transition: opacity var(--transition-smooth);
    }

    .proyecto:hover .proyecto-overlay {
        opacity: 0.1;
    }

    .proyecto-info {
        padding: 1.5rem;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }

        .proyecto-info h3 {
            margin: 0 0 0.5rem 0;
            font-size: 1.3em;
            color: var(--color-heading);
            font-weight: 600;
        }

        .proyecto-info p {
            color: var(--color-text);
            margin: 0 0 1.5rem 0;
            line-height: 1.5;
            flex-grow: 1;
        }

    .proyecto-links {
        display: flex;
        gap: 1rem;
        margin-top: auto;
    }

    .btn-ver-mas {
        background: var(--color-primary);
        color: var(--color-background);
        padding: 0.75rem 1.5rem;
        border-radius: var(--border-radius);
        text-decoration: none;
        font-weight: 600;
        transition: all var(--transition-smooth);
        flex: 1;
        text-align: center;
        border: 2px solid var(--color-primary);
    }

        .btn-ver-mas:hover {
            background: transparent;
            color: var(--color-primary);
            transform: translateY(-2px);
        }

    .github-link {
        background: transparent;
        color: var(--color-text);
        padding: 0.75rem 1.5rem;
        border-radius: var(--border-radius);
        text-decoration: none;
        font-weight: 600;
        transition: all var(--transition-smooth);
        flex: 1;
        text-align: center;
        border: 2px solid var(--color-border);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }

        .github-link:hover {
            border-color: var(--color-primary);
            color: var(--color-primary);
            transform: translateY(-2px);
        }

    @media (max-width: 768px) {
        .galeria {
            grid-template-columns: 1fr;
            padding: 1rem;
            gap: 1.5rem;
        }

        .proyecto-links {
            flex-direction: column;
        }
    }
</style>
