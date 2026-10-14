import { cn } from "../../lib/utils"

export function ScoutMark({ className }: { className?: string }) {
  return <svg viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg" className={cn("w-full h-full", className)} aria-label="Scout"><rect width="400" height="400" rx="88" fill="hsl(var(--primary))" /><circle cx="180" cy="180" r="84" stroke="white" strokeWidth="36" /><path d="M244 244L318 318" stroke="white" strokeWidth="36" strokeLinecap="round" /></svg>
}
