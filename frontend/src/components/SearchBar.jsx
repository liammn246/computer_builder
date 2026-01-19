export function SearchBar({ searchPrompt, setSearchPrompt, showAdvanced, setShowAdvanced }) {
  return (
    <div className="flex items-center space-x-2">
      <input
        type="text"
        placeholder="Type what kind of PC you want..."
        className="grow px-4 py-3 rounded-full border focus:ring-2 focus:ring-blue-400"
        value={searchPrompt}
        onChange={(e) => setSearchPrompt(e.target.value)}
      />
      <button
        onClick={() => setShowAdvanced((v) => !v)}
        className="w-12 h-12 bg-gray-200 rounded-xl hover:bg-gray-300 transition"
      >
        +
      </button>
    </div>
  );
}
