import { useEffect, useState } from "react";
import { SearchBar } from "./components/SearchBar";
import { AdvancedSearch } from "./components/AdvancedSearch";
import { SuggestedBuild } from "./components/SuggestedBuild";

function App() {
  const [showAdvanced, setShowAdvanced] = useState(false);

  const [cpus, setCpus] = useState([]);
  const [gpus, setGpus] = useState([]);

  const [searchPrompt, setSearchPrompt] = useState("");

  const [selectedCpu, setSelectedCpu] = useState("");
  const [selectedGpu, setSelectedGpu] = useState("");

  const [cpuBrand, setCpuBrand] = useState("");
  const [gpuBrand, setGpuBrand] = useState("");
  const [ramSize, setRamSize] = useState("");
  const [budget, setBudget] = useState("");

  const [components, setComponents] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/parts/cpus")
      .then((res) => res.json())
      .then(setCpus)
      .catch(console.error);

    fetch("http://127.0.0.1:8000/parts/gpus")
      .then((res) => res.json())
      .then(setGpus)
      .catch(console.error);
  }, []);

  const normalize = (v) => (v === "" ? null : v);

  const handleGenerateBuild = () => {
    const payload = {
      cpu_name: normalize(selectedCpu),
      gpu_name: normalize(selectedGpu),
      cpu_brand: normalize(cpuBrand),
      gpu_brand: normalize(gpuBrand),
      ram_size: normalize(ramSize),
      budget: normalize(budget),
    };

    fetch("http://127.0.0.1:8000/filter/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then((res) => res.json())
      .then(setComponents)
      .catch(console.error);
  };

  const inputClass = "w-full px-3 py-2 border rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-400";

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-3xl font-bold mb-8 text-center">Build Your PC</h1>

      <div className="mx-auto max-w-7xl flex gap-8 items-start justify-center">
        {/* LEFT PANEL */}
        <div className="flex-1 min-w-0 max-w-3xl">
          {/* Search */}
          <SearchBar
            searchPrompt={searchPrompt}
            setSearchPrompt={setSearchPrompt}
            showAdvanced={showAdvanced}
            setShowAdvanced={setShowAdvanced}
          />

          {/* Advanced */}
          <AdvancedSearch
            showAdvanced={showAdvanced}
            cpus={cpus}
            gpus={gpus}
            selectedCpu={selectedCpu}
            setSelectedCpu={setSelectedCpu}
            selectedGpu={selectedGpu}
            setSelectedGpu={setSelectedGpu}
            cpuBrand={cpuBrand}
            setCpuBrand={setCpuBrand}
            gpuBrand={gpuBrand}
            setGpuBrand={setGpuBrand}
            ramSize={ramSize}
            setRamSize={setRamSize}
            budget={budget}
            setBudget={setBudget}
            onGenerateBuild={handleGenerateBuild}
          />
        </div>

        {/* RIGHT PANEL */}
        <SuggestedBuild components={components} />
      </div>
    </div>
  );
}

export default App;
