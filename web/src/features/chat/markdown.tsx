// Assistant prose. 1code renders with Streamdown + Shiki; here it is react-markdown + remark-gfm
// with the same `prose` class stack from 1code's chat-markdown-renderer.tsx.

import { memo } from "react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import { cn } from "../../lib/utils"

interface MarkdownProps {
  content: string
  size?: "sm" | "md"
  className?: string
  isStreaming?: boolean
}

export const Markdown = memo(function Markdown({ content, size = "md", className, isStreaming }: MarkdownProps) {
  return (
    <div
      className={cn(
        "prose prose-sm max-w-none dark:prose-invert prose-code:before:content-none prose-code:after:content-none",
        "prose-p:my-0 prose-ul:my-0 prose-ol:my-0 prose-li:my-0",
        "prose-hr:my-0",
        "prose-table:my-0",
        "[&>*+*]:mt-3 [&_ul]:pl-5 [&_ol]:pl-5 [&_li+li]:mt-1 [&_blockquote]:not-italic [&_blockquote]:border-l-2 [&_blockquote]:pl-3 [&_blockquote]:text-muted-foreground",
        "[&_code]:rounded [&_code]:bg-muted [&_code]:px-1 [&_code]:py-0.5 [&_code]:font-mono [&_code]:text-[12px] [&_code]:font-normal",
        "[&_pre]:bg-muted [&_pre]:border [&_pre]:rounded-lg [&_pre]:p-3 [&_pre_code]:bg-transparent [&_pre_code]:p-0",
        "[&_a]:text-primary [&_a]:no-underline hover:[&_a]:underline [&_strong]:font-semibold",
        size === "sm" ? "text-xs" : "text-sm leading-relaxed",
        isStreaming && "[&>*:last-child]:after:content-['▍'] [&>*:last-child]:after:ml-0.5 [&>*:last-child]:after:text-muted-foreground/60 [&>*:last-child]:after:animate-pulse",
        className,
      )}
    >
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ node: _n, ...props }) => <a {...props} target="_blank" rel="noopener noreferrer" />,
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
})
