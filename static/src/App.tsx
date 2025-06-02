import React, { useEffect, useRef, useState } from 'react';
import { Brain } from 'lucide-react';
import { AuthForm } from './components/AuthForm';
import { supabase } from './lib/supabase';
import { Toaster } from 'react-hot-toast';

function ParticleCanvas() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles: Array<{
      x: number;
      y: number;
      size: number;
      speedX: number;
      speedY: number;
    }> = [];

    const createParticle = () => {
      return {
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 1.5 + 0.5,
        speedX: (Math.random() - 0.5) * 2,
        speedY: (Math.random() - 0.5) * 2
      };
    };

    for (let i = 0; i < 150; i++) {
      particles.push(createParticle());
    }

    const animate = () => {
      ctx.fillStyle = 'rgba(26, 26, 26, 0.2)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      particles.forEach(particle => {
        ctx.fillStyle = '#00ffcc';
        ctx.beginPath();
        ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
        ctx.fill();

        particle.x += particle.speedX;
        particle.y += particle.speedY;

        if (particle.x < 0) particle.x = canvas.width;
        if (particle.x > canvas.width) particle.x = 0;
        if (particle.y < 0) particle.y = canvas.height;
        if (particle.y > canvas.height) particle.y = 0;
      });

      requestAnimationFrame(animate);
    };

    animate();

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="fixed top-0 left-0 w-full h-full pointer-events-none"
    />
  );
}

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setIsAuthenticated(!!session);
    });

    const { data: { subscription } } = supabase.auth.onAuthStateChange((_event, session) => {
      setIsAuthenticated(!!session);
    });

    return () => subscription.unsubscribe();
  }, []);

  const handleAuthSuccess = () => {
    window.location.href = 'https://dotexe.streamlit.app/';
  };

  return (
    <div className="relative min-h-screen bg-[#1a1a1a] text-white overflow-hidden">
      <ParticleCanvas />
      <Toaster position="top-right" />
      
      <div className="relative z-10 min-h-screen flex flex-col items-center justify-center p-4 sm:p-6 md:p-8">
        <div className="animate-fade-in space-y-6 sm:space-y-8 text-center max-w-xl mx-auto">
          <div className="flex flex-col sm:flex-row items-center justify-center sm:space-x-4 space-y-4 sm:space-y-0">
            <Brain className="w-10 h-10 sm:w-12 sm:h-12 text-[#00ffcc]" />
            <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold font-orbitron tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-[#00ffcc] to-[#00fff2]">
              MindGlow
            </h1>
          </div>
          
          <p className="text-lg sm:text-xl md:text-2xl text-gray-300 font-light px-4">
            Unlock Your Inner Vibe with One Click
          </p>

          {isAuthenticated ? (
            <div className="mt-8">
              <a
                href="https://dotexe.streamlit.app/"
                className="inline-block px-6 sm:px-8 py-3 sm:py-4 text-base sm:text-lg font-semibold text-white bg-transparent border-2 border-[#00ffcc] rounded-full transition-all duration-300 hover:scale-105 hover:bg-[#00ffcc]/10 hover:shadow-[0_0_20px_rgba(0,255,204,0.5)] animate-pulse"
              >
                Get Started
              </a>
            </div>
          ) : (
            <AuthForm onSuccess={handleAuthSuccess} />
          )}
        </div>
      </div>
    </div>
  );
}

export default App;