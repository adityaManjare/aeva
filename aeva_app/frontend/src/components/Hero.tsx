import { Button } from "@/components/ui/button";
import { ArrowRight, Upload, Search, FileText } from "lucide-react";
import heroImage from "@/assets/academic-hero.jpg";

const Hero = () => {
  const scrollToChat = () => {
    const chatSection = document.getElementById('chat');
    if (chatSection) {
      chatSection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section className="relative min-h-[80vh] flex items-center bg-gradient-to-br from-background via-academic-light-rose/20 to-background overflow-hidden">
      <div className="absolute inset-0 bg-grid-pattern opacity-5"></div>
      
      <div className="container relative z-10">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <div className="space-y-8">
            <div className="space-y-4">
              <h1 className="text-4xl md:text-6xl font-bold leading-tight">
                Your AI-Powered
                <span className="block bg-gradient-to-r from-academic-teal to-academic-burgundy bg-clip-text text-transparent">
                  Study Assistant
                </span>
              </h1>
              <p className="text-xl text-muted-foreground leading-relaxed">
                Upload your PDFs, ask questions, and get intelligent answers. 
                StudyMind AI helps you understand complex academic materials with ease.
              </p>
            </div>

            <div className="flex flex-col sm:flex-row gap-4">
              <Button 
                variant="academic" 
                size="lg" 
                className="text-lg px-8 py-6"
                onClick={scrollToChat}
              >
                Start Studying Now
                <ArrowRight className="w-5 h-5" />
              </Button>
              <Button variant="academicOutline" size="lg" className="text-lg px-8 py-6">
                Watch Demo
              </Button>
            </div>

            <div className="flex items-center gap-8 pt-4">
              <div className="flex items-center gap-2">
                <Upload className="w-5 h-5 text-academic-teal" />
                <span className="text-sm text-muted-foreground">Upload PDFs</span>
              </div>
              <div className="flex items-center gap-2">
                <Search className="w-5 h-5 text-academic-burgundy" />
                <span className="text-sm text-muted-foreground">Web Search</span>
              </div>
              <div className="flex items-center gap-2">
                <FileText className="w-5 h-5 text-academic-rose" />
                <span className="text-sm text-muted-foreground">Smart Analysis</span>
              </div>
            </div>
          </div>

          <div className="relative">
            <div className="relative z-10 rounded-2xl overflow-hidden shadow-2xl hover:shadow-3xl transition-all duration-500">
              <img 
                src={heroImage} 
                alt="Academic Study Assistant" 
                className="w-full h-auto object-cover"
              />
            </div>
            <div className="absolute -top-4 -right-4 w-full h-full bg-gradient-to-br from-academic-rose/20 to-academic-burgundy/20 rounded-2xl blur-xl"></div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;