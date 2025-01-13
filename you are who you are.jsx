import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const GameConcept = () => {
  const [selectedTab, setSelectedTab] = useState('concept');

  return (
    <Card className="w-full max-w-4xl bg-white shadow-lg">
      <CardHeader>
        <CardTitle className="text-2xl font-bold text-center">Mirror Maze: Reflections of Self</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          <div className="grid grid-cols-4 gap-2 mb-6">
            <button 
              onClick={() => setSelectedTab('concept')}
              className={`p-2 rounded ${selectedTab === 'concept' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            >
              Concept
            </button>
            <button 
              onClick={() => setSelectedTab('mechanics')}
              className={`p-2 rounded ${selectedTab === 'mechanics' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            >
              Mechanics
            </button>
            <button 
              onClick={() => setSelectedTab('progression')}
              className={`p-2 rounded ${selectedTab === 'progression' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            >
              Progression
            </button>
            <button 
              onClick={() => setSelectedTab('technical')}
              className={`p-2 rounded ${selectedTab === 'technical' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            >
              Technical
            </button>
          </div>

          {selectedTab === 'concept' && (
            <div className="space-y-4">
              <h3 className="text-xl font-semibold">Core Concept</h3>
              <p>A puzzle game where the player navigates through a maze of mirrors, but with a twist - your reflection is your worst enemy and your greatest ally. The player character is a being made of light, consumed by their own self-image.</p>
              
              <h3 className="text-xl font-semibold">Theme Integration</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Mirrors represent self-reflection and obsession with self-image</li>
                <li>The player's light can be both empowering and destructive</li>
                <li>Multiple reflections represent fragmented self-perception</li>
                <li>The maze symbolizes the confusing path of self-discovery</li>
              </ul>
            </div>
          )}

          {selectedTab === 'mechanics' && (
            <div className="space-y-4">
              <h3 className="text-xl font-semibold">Core Mechanics</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Light Beam Control: Player emits light in different directions</li>
                <li>Mirror Manipulation: Rotate and position mirrors to solve puzzles</li>
                <li>Reflection Management: Each reflection creates a duplicate light source</li>
                <li>Energy Balance: Too many reflections drain your energy</li>
              </ul>

              <h3 className="text-xl font-semibold">Puzzle Elements</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Light-activated switches and doors</li>
                <li>Color-mixing mechanics with different reflections</li>
                <li>Time-based challenges requiring multiple reflections</li>
                <li>Shadow zones that need to be illuminated</li>
              </ul>
            </div>
          )}

          {selectedTab === 'progression' && (
            <div className="space-y-4">
              <h3 className="text-xl font-semibold">Level Structure</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Tutorial: Basic light and mirror mechanics</li>
                <li>Early Levels: Single reflection puzzles</li>
                <li>Mid-Game: Multiple reflection management</li>
                <li>Late Game: Complex mirror networks and timing challenges</li>
              </ul>

              <h3 className="text-xl font-semibold">Narrative Integration</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Each level represents a stage of self-realization</li>
                <li>Environmental storytelling through mirror placement</li>
                <li>Visual evolution of the character's light form</li>
                <li>Multiple endings based on reflection management</li>
              </ul>
            </div>
          )}

          {selectedTab === 'technical' && (
            <div className="space-y-4">
              <h3 className="text-xl font-semibold">Technical Requirements</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>2D light ray system with reflection calculations</li>
                <li>Mirror rotation and positioning system</li>
                <li>Efficient reflection management and rendering</li>
                <li>Collision detection for light rays</li>
              </ul>

              <h3 className="text-xl font-semibold">Implementation Plan</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Unity 2D with custom shader for light effects</li>
                <li>Vector-based light calculation system</li>
                <li>Grid-based level design with free mirror placement</li>
                <li>Modular puzzle component system</li>
              </ul>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
};

export default GameConcept;
