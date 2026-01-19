import { SelectRow } from "./SelectRow";

const inputClass = "w-full px-3 py-2 border rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-400";

export function AdvancedSearch({
  showAdvanced,
  cpus,
  gpus,
  selectedCpu,
  setSelectedCpu,
  selectedGpu,
  setSelectedGpu,
  cpuBrand,
  setCpuBrand,
  gpuBrand,
  setGpuBrand,
  ramSize,
  setRamSize,
  budget,
  setBudget,
  onGenerateBuild,
}) {
  return (
    <>
      <div
        className={`my-3 bg-white border rounded-lg shadow-md overflow-hidden transition-all duration-500 ${
          showAdvanced ? "max-h-[600px] opacity-100 p-4" : "max-h-0 opacity-0 p-0"
        }`}
      >
        <div className="flex flex-col gap-3">
          <p className="text-sm text-gray-600">
            Select specific parts or leave blank
          </p>

          <SelectRow label="CPU Name">
            <select
              value={selectedCpu}
              onChange={(e) => setSelectedCpu(e.target.value)}
              className={inputClass}
            >
              <option value="">Any CPU</option>
              {cpus.map((cpu) => (
                <option key={cpu.id} value={cpu.name}>
                  {cpu.name}
                </option>
              ))}
            </select>
          </SelectRow>

          <SelectRow label="GPU Name">
            <select
              value={selectedGpu}
              onChange={(e) => setSelectedGpu(e.target.value)}
              className={inputClass}
            >
              <option value="">Any GPU</option>
              {gpus.map((gpu) => (
                <option key={gpu.id} value={gpu.name}>
                  {gpu.name}
                </option>
              ))}
            </select>
          </SelectRow>

          <SelectRow label="CPU Brand">
            <select
              value={cpuBrand}
              onChange={(e) => setCpuBrand(e.target.value)}
              disabled={!!selectedCpu}
              className={`${inputClass} disabled:bg-gray-100 disabled:text-gray-500 disabled:cursor-not-allowed`}
            >
              <option value="">Any</option>
              <option value="AMD">AMD</option>
              <option value="INTEL">INTEL</option>
            </select>
          </SelectRow>

          <SelectRow label="GPU Brand">
            <select
              value={gpuBrand}
              onChange={(e) => setGpuBrand(e.target.value)}
              disabled={!!selectedGpu}
              className={`${inputClass} disabled:bg-gray-100 disabled:text-gray-500 disabled:cursor-not-allowed`}
            >
              <option value="">Any</option>
              <option value="AMD">AMD</option>
              <option value="NVIDIA">NVIDIA</option>
              <option value="INTEL">INTEL</option>
            </select>
          </SelectRow>

          <SelectRow label="RAM Size">
            <select
              value={ramSize}
              onChange={(e) => setRamSize(e.target.value)}
              className={inputClass}
            >
              <option value="">Any</option>
              <option value="8">8GB</option>
              <option value="16">16GB</option>
              <option value="32">32GB</option>
              <option value="64">64GB</option>
            </select>
          </SelectRow>

          <SelectRow label="Budget">
            <input
              type="number"
              value={budget}
              onChange={(e) => setBudget(e.target.value)}
              className={inputClass}
            />
          </SelectRow>
        </div>
      </div>

      <button
        onClick={onGenerateBuild}
        className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600"
      >
        Generate Build
      </button>
    </>
  );
}
