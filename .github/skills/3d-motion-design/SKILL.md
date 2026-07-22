---
name: 3d-motion-design
description: "Create immersive 3D motion experiences and scroll-driven web animations using Three.js, React Three Fiber (R3F), Spline, GSAP, and related front-end tooling. Use for landing pages, portfolios, product showcases, and interactive storytelling."
argument-hint: "Build a 3D motion experience with Three.js, R3F, Spline, and scroll animations"
user-invocable: true
disable-model-invocation: false
---

# 3D Motion Design and Scroll Animation

## When to Use

- You need a rich interactive 3D experience for a website or app.
- You want animated scenes that respond to scroll, mouse movement, or user interaction.
- You need to choose between lightweight visual prototyping and highly custom 3D development.

## Core Approach

### 1. Define the experience

- Clarify the goal: storytelling, product showcase, portfolio, hero section, or interactive demo.
- Decide whether the experience should be:
  - fully custom and code-driven,
  - React-integrated,
  - or rapid-prototyped in a visual editor.

### 2. Choose the right tool

- Use Three.js when you need full control over geometry, camera, lighting, shaders, and animation.
- Use React Three Fiber (R3F) when the project is already built with React and you want 3D scenes to fit naturally into component-based UI.
- Use Spline when you want to build polished 3D scenes quickly with an editor-based workflow.
- Use GSAP, Lenis, ScrollTrigger, or similar libraries for scroll-based motion and timeline control.

### 3. Build the scene structure

- Create a clear scene hierarchy: camera, lights, models, environment, and effects.
- Keep models and assets optimized for the web.
- Add interaction layers such as hover states, click events, and motion responsiveness.

### 4. Add scroll animation

- Tie motion to scroll progress using scroll-based triggers.
- Animate camera position, object transforms, opacity, scale, and scene composition.
- Use easing and staggered motion to make transitions feel polished.

### 5. Optimize for performance

- Reduce unnecessary geometry and textures.
- Use instancing or lower-polygon assets where possible.
- Avoid heavy re-renders in React-based scenes.
- Test on mobile and desktop to ensure smooth performance.

## Recommended Workflow

1. Start with the content and motion story.
2. Pick the best stack for the task:
   - Spline for fast visual prototyping
   - Three.js for custom scenes
   - R3F for React integration
   - GSAP + ScrollTrigger for scroll-driven choreography
3. Create a simple prototype first.
4. Add interaction and scroll-linked motion.
5. Polish lighting, camera movement, and timing.
6. Test responsiveness and performance.

## Quality Checklist

- The experience feels intentional and polished.
- 3D motion supports the content rather than overwhelming it.
- Scroll animation is smooth and readable.
- The build remains performant on common devices.
- The implementation is maintainable and easy to extend.

## Implementation Notes

- For production-grade custom scenes, prefer Three.js or R3F.
- For quick and visually striking concepts, Spline is often the fastest path.
- For advanced scroll storytelling, combine a 3D scene with GSAP and ScrollTrigger.
- If the project is React-based, R3F is usually the best fit.

## Example Prompts

- "Create a 3D hero section with orbiting elements and smooth scroll transitions."
- "Build a product showcase using React Three Fiber and scroll-driven camera animation."
- "Design a polished Spline-based landing page with interactive motion and parallax effects."
- "Add scroll-based reveal animations to a Three.js scene with GSAP."
