import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const GameConcept = () => {
  const [selectedTab, setSelectedTab] = useState('concept');

  return (
    <Card className="w-full max-w-4xl bg-slate-900 text-white">
      <CardHeader>
        <CardTitle className="text-2xl font-bold text-center text-red-500">The Narcissist's Descent: Worse and Worse</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          <div className="grid grid-cols-4 gap-2 mb-6">
            <button 
              onClick={() => setSelectedTab('concept')}
              className={`p-2 rounded ${selectedTab === 'concept' ? 'bg-red-800' : 'bg-gray-800'}`}
            >
              Core Premise
            </button>
            <button 
              onClick={() => setSelectedTab('mechanics')}
              className={`p-2 rounded ${selectedTab === 'mechanics' ? 'bg-red-800' : 'bg-gray-800'}`}
            >
              Mechanics
            </button>
            <button 
              onClick={() => setSelectedTab('progression')}
              className={`p-2 rounded ${selectedTab === 'progression' ? 'bg-red-800' : 'bg-gray-800'}`}
            >
              Progression
            </button>
            <button 
              onClick={() => setSelectedTab('technical')}
              className={`p-2 rounded ${selectedTab === 'technical' ? 'bg-red-800' : 'bg-gray-800'}`}
            >
              Implementation
            </button>
          </div>

          {selectedTab === 'concept' && (
            <div className="space-y-4">
              <h3 className="text-xl font-semibold text-red-400">Core Concept</h3>
              <p>A psychological horror game where you play as a narcissist who must manipulate others to maintain their self-image. Each "success" makes things progressively worse, forcing increasingly destructive behaviors.</p>
              
              <h3 className="text-xl font-semibold text-red-400">Deterioration Mechanics</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Every "win" actually damages your character's psyche</li>
                <li>Success requires more extreme manipulation each time</li>
                <li>NPCs become increasingly traumatized by interactions</li>
                <li>The environment reflects psychological deterioration</li>
              </ul>
            </div>
          )}

          {selectedTab === 'mechanics' && (
            <div className="space-y-4">
              <h3 className="text-xl font-semibold text-red-400">Core Systems</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Supply: NPCs' emotional resources you can drain</li>
                <li>Manipulation Tactics: Gaslighting, Love Bombing, Triangulation</li>
                <li>False Self Meter: Must be maintained through others' suffering</li>
                <li>Reality Distortion: Environment warps with each "victory"</li>
              </ul>

              <h3 className="text-xl font-semibold text-red-400">Interaction System</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Dialog choices become more overtly abusive over time</li>
                <li>Previously "successful" tactics stop working</li>
                <li>Must find new victims as old ones break down</li>
                <li>Environment becomes more nightmarish with progress</li>
              </ul>
            </div>
          )}

          {selectedTab === 'progression' && (
            <div className="space-y-4">
              <h3 className="text-xl font-semibold text-red-400">Descent Structure</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Level 1: Subtle manipulation and charm</li>
                <li>Level 2: Overt emotional exploitation</li>
                <li>Level 3: Destructive relationship patterns</li>
                <li>Level 4: Complete psychological warfare</li>
                <li>Final Stage: Total psychotic break</li>
              </ul>

              <h3 className="text-xl font-semibold text-red-400">Environmental Evolution</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>World becomes more twisted with each "success"</li>
                <li>Reality starts breaking down visually</li>
                <li>NPCs show visible trauma and deterioration</li>
                <li>No positive ending possible - only degrees of horror</li>
              </ul>
            </div>
          )}

          {selectedTab === 'technical' && (
            <div className="space-y-4">
              <h3 className="text-xl font-semibold text-red-400">Core Systems</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Dynamic NPC trauma system</li>
                <li>Progressive environment distortion shader</li>
                <li>Adaptive dialog system that grows more twisted</li>
                <li>Reality warping visual effects</li>
              </ul>

              <h3 className="text-xl font-semibold text-red-400">Implementation</h3>
              <ul className="list-disc pl-6 space-y-2">
                <li>Unity with custom shader graph for distortions</li>
                <li>Branching dialog system with deterioration tracking</li>
                <li>Dynamic NPC state machine with trauma accumulation</li>
                <li>Procedural environment corruption system</li>
              </ul>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
};

export default GameConcept;
