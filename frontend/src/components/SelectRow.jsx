export function SelectRow({ label, children }) {
  return (
    <div className="flex items-center gap-4">
      <span className="w-28 text-sm text-right text-gray-700">{label}:</span>
      <div className="flex-1">{children}</div>
    </div>
  );
}
