-- Pandoc preserves Markdown's default left table alignment in LaTeX output,
-- even when the document direction is RTL. Convert those columns to right
-- alignment for RTL documents while preserving explicit centered columns.

local function align_table_right(table)
  for index, colspec in ipairs(table.colspecs) do
    local alignment = colspec[1]
    if alignment == pandoc.AlignDefault or alignment == pandoc.AlignLeft then
      table.colspecs[index] = { pandoc.AlignRight, colspec[2] }
    end
  end

  return table
end

function Pandoc(document)
  if pandoc.utils.stringify(document.meta.dir) ~= "rtl" then
    return document
  end

  return document:walk({ Table = align_table_right })
end
