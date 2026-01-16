import { useEffect, useState } from "react";

function App() {
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [cpus, setCpus] = useState([]); // Will be an array of objects
  const [gpus, setGpus] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/parts/cpus")
      .then((response) => response.json())
      .then((data) => setCpus(data))
      .catch((error) => console.error("Error fetching CPUs:", error));
    fetch("http://127.0.0.1:8000/parts/gpus")
      .then((response) => response.json())
      .then((data) => setGpus(data))
      .catch((error) => console.error("Error fetching GPUs:", error));
  }, []);
  //Search prompt
  const [searchPrompt, setSearchPrompt] = useState("");
  // Specific part selections
  const [selectedCpu, setSelectedCpu] = useState("");
  const [selectedGpu, setSelectedGpu] = useState("");
  // Optional specifications
  const [cpuBrand, setCpuBrand] = useState("");
  const [gpuBrand, setGpuBrand] = useState("");
  const [ramSize, setRamSize] = useState("");
  const [budget, setBudget] = useState("");
  // Build parts
  const [components, setComponents] = useState(null);

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
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then((response) => response.json())
      .then((data) => setComponents(data))
      .catch((error) => console.error("Error fetching components:", error));
    console.log(components)
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-start bg-gray-50 p-6">
      <h1 className="text-3xl font-bold mb-8">Build Your PC</h1>

      {/* Search Bar Section */}
      <div className="flex items-center space-x-2 w-full max-w-xl">
        <input
          type="text"
          placeholder="Type what kind of PC you want..."
          className="grow px-4 py-3 rounded-full border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400"
          value={searchPrompt}
          onChange={(e) => setSearchPrompt(e.target.value)}
        />
        <button
          onClick={() => setShowAdvanced(!showAdvanced)}
          className="w-12 h-12 flex items-center justify-center bg-gray-200 rounded-xl hover:bg-gray-300 transition"
        >
          +
        </button>
      </div>

      {/* Advanced Search Section with flexible animation */}
      <div
        className={`mt-4 w-full max-w-xl bg-white shadow-md rounded-lg border border-gray-200 overflow-hidden transition-all duration-500 ease-in-out ${
          showAdvanced ? "max-h-500 opacity-100 p-4" : "max-h-0 opacity-0 p-0"
        }`}>
        <div className="flex flex-col gap-3">
          <p>If you have specific parts that you want to incorporate, select them here:</p>

          <div className="flex items-center gap-4">
            <span className="w-28 text-sm font-medium text-gray-700 text-right"> CPU Name: </span>
            <select value={selectedCpu} onChange={(e) => setSelectedCpu(e.target.value)} className="flex-1 px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400">
              <option value="">Any CPU</option>
              {cpus.map((cpu) => (
                <option key={cpu.id} value={cpu.name}>
                  {cpu.name}
                </option>
              ))}
            </select>
          </div>



          <div className="flex items-center gap-4">
            <span className="w-28 text-sm font-medium text-gray-700 text-right"> GPU Name: </span>
            <select value={selectedGpu} onChange={(e) => setSelectedGpu(e.target.value)} className="flex-1 px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400">
              <option value="">Any GPU</option>
              {gpus.map((gpu) => (
                <option key={gpu.id} value={gpu.name}>
                  {gpu.name}
                </option>
              ))}
            </select>
          </div>

          {/* Non descript part specification */}
          {/* Eventually, the fields will need to be larger, including stats like vram, cores, .... */}
          {/* If a specific field is used, cross out that part from the optional fields */}
          <p>Specify what type of parts you want here: (Optional)</p>
          <div className="flex items-center gap-4">
            <span className="w-28 text-sm font-medium text-gray-700 text-right"> CPU Brand: </span>
            <select value={cpuBrand} onChange={(e) => setCpuBrand(e.target.value)} disabled={normalize(selectedCpu) != null} className="flex-1 px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 disabled:bg-gray-100 disabled:text-gray-500 disabled:cursor-not-allowed">
              <option value="">Any CPU Brand</option>
              <option value="AMD">AMD</option> 
              <option value="INTEL">INTEL</option>
            </select>
          </div>

          <div className="flex items-center gap-4">
            <span className="w-28 text-sm font-medium text-gray-700 text-right"> GPU Brand: </span>
            <select value={gpuBrand} onChange={(e) => setGpuBrand(e.target.value)} disabled={normalize(selectedGpu) != null} className="flex-1 px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 disabled:bg-gray-100 disabled:text-gray-500 disabled:cursor-not-allowed">
              <option value="">Any GPU Brand</option>
              <option value="AMD">AMD</option>
              <option value="NVIDIA">NVIDIA</option>
              <option value="INTEL">INTEL</option>
            </select>
          </div>

          <div className="flex items-center gap-4">
            <span className="w-28 text-sm font-medium text-gray-700 text-right"> RAM Size: </span>
            <select value={ramSize} onChange={(e) => setRamSize(e.target.value)} className="flex-1 px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400">
              <option value="">Any RAM size</option>
              <option value="8">8GB</option>
              <option value="16">16GB</option>
              <option value="32">32GB</option>
              <option value="64">64GB</option>
            </select>
          </div>

          <input value={budget} onChange={(e) => setBudget(e.target.value)} type="number" placeholder="Budget" className="px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"/>

          <button onClick={() => handleGenerateBuild()} className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition">
            Generate Build
          </button>
        </div>
      </div>

      {/* Placeholder Suggested Build */}
      {components && (
        <div className="mt-8 w-full max-w-xl space-y-3">
          <h2 className="text-xl font-semibold">Suggested Build</h2>

          <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            CPU: {components.cpus?.[0]?.name ?? "—"}
          </div>

          <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            GPU: {components.gpus?.[0]?.name ?? "—"}
          </div>

          <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            RAM: {components.ram ?? "—"}
          </div>

          <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            Storage: {components.storage ?? "—"}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
