---
slug: "nicole-gesare-onyiego"
url: "https://devpost.com/software/nicole-gesare-onyiego"
title: "Nicole Gesare Onyiego"
hackathon: "PortXFolio"
organization: "BurgerOS"
winner: true
words: 666
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Nicole Gesare Onyiego

> My Portfolio : Code-Design-Innovate

[Devpost](https://devpost.com/software/nicole-gesare-onyiego) · hackathon [[PortXFolio]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]]

**stack** framer, javascript, nextjs, python, react, tailwind, three.js, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- technologies and development
- key development techniques
- achievements and lessons
- what’s next for nicole gesare onyiego

## Body

Nicole Gesare Onyiego’s Portfolio: Development, Organization, and Inspirations Inspiration As a multidisciplinary creator—game developer, artist, and web developer—I envisioned a portfolio that not only showcases my work but also tells my story . I wanted an experience that merges interactivity, aesthetics, and personalization to reflect my diverse passions in game development, web design, IoT, and art. Rather than going with a generic layout, I aimed to build something vibrant, immersive, and technically creative . My design inspirations pulled from: Cyberpunk Aesthetics : Neon hues, glitch effects, and futuristic UIs inspired by Cyberpunk 2077 and sci-fi design systems Creative Interactive Portfolios : Bruno Imbrizi’s particle art and the 3D web storytelling of sites like Sharyap.com and Awwwards winners CLI and Terminal Themes : Text animations and command-line-styled prompts for a developer-friendly vibe Sci-fi UI Design : Holographic interfaces, data visualizations, and “system boot” narratives What It Does My portfolio is an interactive web experience designed to invite visitors into my world: Dynamic Homepage : Smooth scroll, animated transitions, and cyberpunk effects Projects Section : Live previews, GitHub links, category tags About Timeline : Chronicles my journey through engineering, art, and innovation AI Portfolio Assistant : OpenAI-powered chatbot to guide visitors Theme Switcher : Light, dark, and creative (cyberpunk) modes Responsive Design : Mobile-first layouts with fluid responsiveness Accessibility Built-in : Alt-text, keyboard navigation, and contrast controls Blog Area : Technical insights, development lessons, and personal reflections Technologies and Development Core Stack Frontend : Next.js (React framework) with TypeScript Styling : Tailwind CSS and custom CSS for cyberpunk theme Backend : Flask API serving dynamic content (e.g., blog, projects) 3D + Animation : React Three Fiber (Three.js), @react-three/drei, Framer Motion Hosting : Vercel (frontend), Render (backend) Auth (Planned) : JWT for future CMS-style admin panel Extras : OpenAI API, Formik for forms, LottieFiles for animations Component Architecture Atomic Design : Small components building into complex sections Dynamic Imports : Used for heavy/3D components to optimize load times Client vs Server Components : Clear separation for performance Progressive Enhancement : Core experience works without JS; JS enhances Project Structure /app # Next.js App Router /api # Flask-integrated API routes /layout.tsx # Root layout /page.tsx # Main landing page /components /sections # Hero, About, Projects, etc. /three # Three.js components /ui # Reusable UI (shadcn/ui) /loading # Custom loading screens /public /fonts # Custom typography /images # Static assets /hooks # Custom logic (e.g., useMobile, useTheme) Key Development Techniques Responsive Layout <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"> 3D Integration (React Three Fiber) function ProfileSphere() { const meshRef = useRef() useFrame(({ clock }) => { if (meshRef.current) { meshRef.current.rotation.y = clock.getElapsedTime() * 0.1 } }) return ( <mesh ref={meshRef}> <circleGeometry args={[2, 64]} /> <meshStandardMaterial /> </mesh> ) } Theme System (Cyberpunk Mode) .cyberpunk { --background: 230 35% 7%; --primary: 320 100% 60%; } Performance Optimizations Dynamic imports for heavy assets Lazy loading images with fallbacks State-based conditional rendering to avoid unnecessary loads Cleanup of listeners on useEffect Custom Hook Example export const useMobile = () => { const [isMobile, setIsMobile] = useState(false) useEffect(() => { const handleResize = () => setIsMobile(window.innerWidth < 768) handleResize() window.addEventListener("resize", handleResize) return () => window.removeEventListener("resize", handleResize) }, []) return isMobile } Achievements and Lessons Accomplishments Created a visually expressive, technically rich portfolio Seamlessly merged storytelling and interactivity Integrated AI meaningfully (not just as a gimmick) <2s load time on desktop via image optimization and code splitting Positive feedback from mentors and peers on its usability and uniqueness Key Learnings Combining Framer Motion + Three.js for high-impact visuals Accessibility goes beyond just alt-text—it’s a design mindset Strong frontend-backend coordination using fetch/Flask Design thinking: how users feel matters as much as what they do Telling a story through code is as powerful as the features themselves What’s Next for Nicole Gesare Onyiego Add a digital/traditional art gallery with filtering by medium Expand blog into a learning hub on creative tech Build an immersive Unity WebGL “game resume” Develop a full CMS dashboard to manage content and analytics <div