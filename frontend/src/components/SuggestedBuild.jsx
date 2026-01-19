export function SuggestedBuild({ components }) {
  if (!components) return null;

  return (
    <div className="w-96 sticky top-6">
      <h2 className="text-xl font-semibold mb-4">Suggested Build</h2>

      {[
        ["CPU", components.cpus?.[0]?.name],
        ["GPU", components.gpus?.[0]?.name],
        ["RAM", components.ram],
        ["Storage", components.storage],
      ].map(([label, value]) => (
        <div key={label} className="bg-white p-4 mb-3 border rounded-lg">
          <span className="font-medium">{label}:</span> {value ?? "—"}
        </div>
      ))}
    </div>
  );
}
