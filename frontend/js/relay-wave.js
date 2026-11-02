/**
 * js/relay-wave.js — GetLayers "Relay" Signature Green Light Wave
 * 
 * High-performance WebGL & Canvas Aurora Stream Shader.
 * Recreates the exact luminous, silky green/lime undulating wave of light
 * running continuously behind the interface, as featured in GetLayers Relay.
 */

(function () {
  'use strict';

  // ══════════════════════════════════════════════════════════════
  // GLSL SHADERS FOR RELAY GREEN LIGHT WAVE
  // ══════════════════════════════════════════════════════════════

  const VERTEX_SHADER_SRC = `
    attribute vec2 a_position;
    varying vec2 v_uv;
    void main() {
      v_uv = (a_position + 1.0) * 0.5;
      gl_Position = vec4(a_position, 0.0, 1.0);
    }
  `;

  const FRAGMENT_SHADER_SRC = `
    precision highp float;
    varying vec2 v_uv;

    uniform vec2 u_resolution;
    uniform float u_time;
    uniform float u_scroll;
    uniform vec2 u_mouse;

    // Organic hash & noise functions
    float hash(vec2 p) {
      p = fract(p * vec2(234.34, 435.345));
      p += dot(p, p + 34.23);
      return fract(p.x * p.y);
    }

    float noise(vec2 p) {
      vec2 i = floor(p);
      vec2 f = fract(p);
      f = f * f * (3.0 - 2.0 * f);
      float a = hash(i);
      float b = hash(i + vec2(1.0, 0.0));
      float c = hash(i + vec2(0.0, 1.0));
      float d = hash(i + vec2(1.0, 1.0));
      return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
    }

    void main() {
      // Screen space coords: aspect ratio corrected
      vec2 st = gl_FragCoord.xy / u_resolution.xy;
      float aspect = u_resolution.x / u_resolution.y;
      
      // Normalized coords (-1 to 1)
      vec2 p = (st * 2.0 - 1.0);
      p.x *= aspect;

      // Base time with organic variation
      float t = u_time * 0.35;
      float scrollFactor = u_scroll * 3.14159 * 2.0;
      float mouseX = (u_mouse.x / u_resolution.x - 0.5) * 0.8;
      float mouseY = (u_mouse.y / u_resolution.y - 0.5) * 0.8;

      // Pitch black background base
      vec3 finalColor = vec3(0.0, 0.0, 0.0);

      // Color Palette: Pure GetLayers Relay Lime & Aurora Glow
      vec3 coreLime   = vec3(0.85, 1.0, 0.05);   // #CCFF00 Neon Lime core
      vec3 auroraCyan = vec3(0.0, 0.96, 0.63);   // #00F5A0 Electric Emerald
      vec3 deepGreen  = vec3(0.04, 0.55, 0.28);  // #059669 Forest Glow
      vec3 mistColor  = vec3(0.02, 0.22, 0.12);  // #022c22 Ambient atmospheric mist

      // ── Stream Spine Geometry ─────────────────────────────────
      // S-curve running diagonally from top-left through center to bottom-right
      float yCoord = st.y;
      
      // Primary wave spine with harmonic sub-oscillations
      float spineX = 0.28 + sin(yCoord * 2.4 - t * 0.7 + scrollFactor * 0.8) * 0.22
                          + cos(yCoord * 4.6 + t * 0.5) * 0.09
                          + sin(yCoord * 8.2 - t * 1.1) * 0.035
                          + mouseX * 0.15 * (1.0 - yCoord);

      // Procedural silky fluid undulation
      float fluid = noise(vec2(yCoord * 3.5 - t * 0.4, t * 0.3)) * 0.07;
      spineX += fluid;

      // ── Volumetric Atmospheric Glow ───────────────────────────
      float distSpine = abs(st.x - spineX);
      float broadGlow = exp(-distSpine * 4.2) * 0.45;
      float wideMist  = exp(-distSpine * 1.8) * 0.25;

      finalColor += mistColor * wideMist;
      finalColor += deepGreen * broadGlow;

      // ── Multi-Layered Silky Green Ribbons ─────────────────────
      // Render 6 braided glowing wave strands
      for (int i = 0; i < 6; i++) {
        float fi = float(i);
        float phase = fi * 1.15;
        float speed = 0.6 + fi * 0.12;
        float amp = 0.04 + fi * 0.018;

        // Individual strand displacement
        float strandX = spineX + sin(yCoord * (3.8 + fi * 1.4) + t * speed + phase + scrollFactor * 0.5) * amp
                               + cos(yCoord * (7.2 + fi * 2.0) - t * (speed * 0.7)) * (amp * 0.45);

        float d = abs(st.x - strandX);

        // Core laser sharpness & soft bloom
        float core = 0.0016 / (d + 0.0028);
        float bloom = 0.018 / (d * d * 38.0 + 0.06);

        // Modulate color from lime to cyan across strands
        vec3 strandColor = mix(coreLime, auroraCyan, sin(fi * 0.8 + yCoord * 3.0 + t) * 0.5 + 0.5);

        // Additive lighting accumulation
        finalColor += strandColor * (core * 0.45 + bloom * 0.35);
      }

      // ── Second Harmonic Wave (Cross-interference ribbon) ──────
      // A softer secondary stream that weaves gently across the main spine
      float wave2X = 0.58 + sin(yCoord * 1.8 + t * 0.4 - scrollFactor * 0.6) * 0.28
                          + cos(yCoord * 3.5 - t * 0.5) * 0.12;
      float d2 = abs(st.x - wave2X);
      float glow2 = 0.012 / (d2 * d2 * 25.0 + 0.08);
      float core2 = 0.0012 / (d2 + 0.004);
      finalColor += mix(auroraCyan, deepGreen, 0.4) * (core2 * 0.3 + glow2 * 0.25);

      // Subtle atmospheric vignette at the edges to preserve pitch-black frame
      float vignette = smoothstep(1.3, 0.2, length(p * vec2(0.8, 1.0)));
      finalColor *= vignette;

      // Soft ceiling clamp
      finalColor = clamp(finalColor, 0.0, 1.0);

      gl_FragColor = vec4(finalColor, 1.0);
    }
  `;

  // ══════════════════════════════════════════════════════════════
  // RENDERER CONTROLLER
  // ══════════════════════════════════════════════════════════════

  class RelayWaveRenderer {
    constructor(canvas) {
      this.canvas = canvas;
      this.gl = null;
      this.ctx2d = null;
      this.program = null;
      this.uniforms = {};
      this.startTime = performance.now();
      this.targetScroll = 0;
      this.currentScroll = 0;
      this.targetMouse = { x: window.innerWidth * 0.5, y: window.innerHeight * 0.5 };
      this.currentMouse = { x: window.innerWidth * 0.5, y: window.innerHeight * 0.5 };
      this.isRunning = false;
      this.isWebGL = false;

      this.init();
    }

    init() {
      // Attempt WebGL
      try {
        const gl = this.canvas.getContext('webgl', {
          powerPreference: 'high-performance',
          alpha: false,
          antialias: true,
          preserveDrawingBuffer: false
        }) || this.canvas.getContext('experimental-webgl');

        if (gl && this.initWebGL(gl)) {
          this.gl = gl;
          this.isWebGL = true;
        }
      } catch (err) {
        console.warn('[Relay Wave] WebGL initialization failed, switching to 2D Canvas fallback:', err);
      }

      // If WebGL failed, setup 2D Canvas Fallback
      if (!this.isWebGL) {
        this.ctx2d = this.canvas.getContext('2d');
      }

      this.resize();
      this.bindEvents();
      this.start();
    }

    initWebGL(gl) {
      const vShader = this.compileShader(gl, gl.VERTEX_SHADER, VERTEX_SHADER_SRC);
      const fShader = this.compileShader(gl, gl.FRAGMENT_SHADER, FRAGMENT_SHADER_SRC);
      if (!vShader || !fShader) return false;

      const program = gl.createProgram();
      gl.attachShader(program, vShader);
      gl.attachShader(program, fShader);
      gl.linkProgram(program);

      if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
        console.error('[Relay Wave] Shader link error:', gl.getProgramInfoLog(program));
        return false;
      }

      this.program = program;
      gl.useProgram(program);

      // Quad buffer (-1 to +1)
      const quad = new Float32Array([
        -1, -1,
         1, -1,
        -1,  1,
        -1,  1,
         1, -1,
         1,  1
      ]);
      const buffer = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
      gl.bufferData(gl.ARRAY_BUFFER, quad, gl.STATIC_DRAW);

      const aPosition = gl.getAttribLocation(program, 'a_position');
      gl.enableVertexAttribArray(aPosition);
      gl.vertexAttribPointer(aPosition, 2, gl.FLOAT, false, 0, 0);

      // Uniform locations
      this.uniforms = {
        resolution: gl.getUniformLocation(program, 'u_resolution'),
        time: gl.getUniformLocation(program, 'u_time'),
        scroll: gl.getUniformLocation(program, 'u_scroll'),
        mouse: gl.getUniformLocation(program, 'u_mouse'),
      };

      return true;
    }

    compileShader(gl, type, src) {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, src);
      gl.compileShader(shader);
      if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error('[Relay Wave] Shader compile error:', gl.getShaderInfoLog(shader));
        gl.deleteShader(shader);
        return null;
      }
      return shader;
    }

    resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const w = window.innerWidth;
      const h = window.innerHeight;

      this.canvas.width = Math.floor(w * dpr);
      this.canvas.height = Math.floor(h * dpr);
      this.canvas.style.width = w + 'px';
      this.canvas.style.height = h + 'px';

      if (this.isWebGL && this.gl) {
        this.gl.viewport(0, 0, this.canvas.width, this.canvas.height);
      }
    }

    bindEvents() {
      window.addEventListener('resize', () => this.resize(), { passive: true });

      window.addEventListener('scroll', () => {
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        this.targetScroll = docHeight > 0 ? (window.scrollY / docHeight) : 0;
      }, { passive: true });

      window.addEventListener('mousemove', (e) => {
        this.targetMouse.x = e.clientX;
        this.targetMouse.y = e.clientY;
      }, { passive: true });

      // Pause when tab is hidden to save energy
      document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
          this.stop();
        } else {
          this.start();
        }
      });
    }

    start() {
      if (this.isRunning) return;
      this.isRunning = true;
      const loop = (now) => {
        if (!this.isRunning) return;
        this.render(now);
        requestAnimationFrame(loop);
      };
      requestAnimationFrame(loop);
    }

    stop() {
      this.isRunning = false;
    }

    render(now) {
      const elapsed = (now - this.startTime) * 0.001;

      // Smooth lerp for scroll and mouse
      this.currentScroll += (this.targetScroll - this.currentScroll) * 0.05;
      this.currentMouse.x += (this.targetMouse.x - this.currentMouse.x) * 0.05;
      this.currentMouse.y += (this.targetMouse.y - this.currentMouse.y) * 0.05;

      if (this.isWebGL && this.gl && this.program) {
        const gl = this.gl;
        gl.useProgram(this.program);

        gl.uniform2f(this.uniforms.resolution, this.canvas.width, this.canvas.height);
        gl.uniform1f(this.uniforms.time, elapsed);
        gl.uniform1f(this.uniforms.scroll, this.currentScroll);
        gl.uniform2f(this.uniforms.mouse, this.currentMouse.x * (this.canvas.width / window.innerWidth), (window.innerHeight - this.currentMouse.y) * (this.canvas.height / window.innerHeight));

        gl.drawArrays(gl.TRIANGLES, 0, 6);
      } else if (this.ctx2d) {
        this.render2DFallback(elapsed);
      }
    }

    // ── High-Performance 2D Canvas Fallback ─────────────────────
    render2DFallback(t) {
      const ctx = this.ctx2d;
      const w = this.canvas.width;
      const h = this.canvas.height;

      // Dark background with slight clear trail
      ctx.fillStyle = '#000000';
      ctx.fillRect(0, 0, w, h);

      ctx.save();
      ctx.globalCompositeOperation = 'screen';

      const ribbonCount = 5;
      for (let r = 0; r < ribbonCount; r++) {
        ctx.beginPath();
        const baseOffset = (w * 0.35) + Math.sin(t * 0.5 + r) * (w * 0.1);
        const amp = 80 + r * 30;
        const freq = 0.0025 + r * 0.0005;

        for (let y = 0; y <= h; y += 12) {
          const x = baseOffset + Math.sin(y * freq + t * (0.8 + r * 0.1) + this.currentScroll * 4) * amp;
          if (y === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }

        const grad = ctx.createLinearGradient(0, 0, w, h);
        grad.addColorStop(0, 'rgba(0, 245, 160, 0.4)');
        grad.addColorStop(0.5, 'rgba(204, 255, 0, 0.85)');
        grad.addColorStop(1, 'rgba(5, 150, 105, 0.3)');

        ctx.strokeStyle = grad;
        ctx.lineWidth = 14 - r * 2;
        ctx.shadowColor = '#CCFF00';
        ctx.shadowBlur = 32 - r * 4;
        ctx.stroke();
      }

      ctx.restore();
    }
  }

  // ══════════════════════════════════════════════════════════════
  // AUTO-INITIALIZE ON DOM READY
  // ══════════════════════════════════════════════════════════════

  function init() {
    let canvas = document.getElementById('relay-wave-canvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'relay-wave-canvas';
      canvas.className = 'relay-wave-canvas';
      canvas.setAttribute('aria-hidden', 'true');
      document.body.prepend(canvas);
    }

    window._relayWaveInstance = new RelayWaveRenderer(canvas);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
