-- Preserve Latin phrases within RTL text, and keep Latin-only tables (such
-- as the contributor list) in LTR order with explicit, wrapping columns.

local function contains_rtl(text)
  for _, codepoint in utf8.codes(text) do
    if (codepoint >= 0x0590 and codepoint <= 0x08ff)
      or (codepoint >= 0xfb1d and codepoint <= 0xfdff)
      or (codepoint >= 0xfe70 and codepoint <= 0xfeff) then
      return true
    end
  end
  return false
end

local function is_latin(text)
  return text:match('[A-Za-z0-9]') ~= nil and not contains_rtl(text)
end

local function isolate_latin(inlines)
  local result = pandoc.List()
  local run = pandoc.List()
  local has_latin = false

  local function flush()
    -- Leave surrounding whitespace outside the directional span.
    local trailing = pandoc.List()
    while #run > 0 and (run[#run].tag == 'Space' or run[#run].tag == 'SoftBreak') do
      trailing:insert(1, run:remove())
    end
    if has_latin then
      result:insert(pandoc.Span(run, {dir = 'ltr'}))
    else
      result:extend(run)
    end
    result:extend(trailing)
    run = pandoc.List()
    has_latin = false
  end

  for _, inline in ipairs(inlines) do
    local text = pandoc.utils.stringify(inline)
    if contains_rtl(text) then
      flush()
      result:insert(inline)
    elseif is_latin(text) or #run > 0 then
      run:insert(inline)
      has_latin = has_latin or is_latin(text)
    else
      result:insert(inline)
    end
  end
  flush()
  return result
end

local function align_table_right(table)
  if is_latin(pandoc.utils.stringify(table)) then
    for index, _ in ipairs(table.colspecs) do
      table.colspecs[index] = {pandoc.AlignLeft, 1 / #table.colspecs}
    end
    -- Do not add inline LTR boxes inside this table: they prevent names
    -- from wrapping within the fixed-width cells.
    return pandoc.Div({table}, {dir = 'ltr'}), false
  end
  for index, colspec in ipairs(table.colspecs) do
    local alignment = colspec[1]
    if alignment == pandoc.AlignDefault or alignment == pandoc.AlignLeft then
      table.colspecs[index] = { pandoc.AlignRight, colspec[2] }
    end
  end

  return table
end

function Pandoc(document)
  local direction = document.meta.dir
  if direction == nil or pandoc.utils.stringify(direction) ~= "rtl" then
    return document
  end

  -- Font names, language codes, paths, and other machine-readable metadata
  -- must never acquire directional markup.
  local metadata = document.meta
  document.meta = {}
  document = document:walk({
    traverse = 'topdown',
    Table = align_table_right,
    Span = function(span)
      if span.attributes.dir == 'ltr' then
        return span, false
      end
    end,
    Para = function(paragraph)
      if is_latin(pandoc.utils.stringify(paragraph)) then
        return pandoc.Div({paragraph}, {dir = 'ltr'}), false
      end
    end,
    Inlines = isolate_latin,
  })
  document.meta = metadata
  local title = metadata.title
  for _, key in ipairs({'title', 'subtitle', 'date', 'header-left', 'header-center', 'header-right'}) do
    local value = metadata[key]
    if value and is_latin(pandoc.utils.stringify(value)) then
      document.meta[key] = pandoc.MetaInlines({
        pandoc.Span({pandoc.Str(pandoc.utils.stringify(value))}, {dir = 'ltr'})
      })
    end
  end
  if title and is_latin(pandoc.utils.stringify(title)) then
    -- The large cover title needs a wrapping LTR paragraph, rather than
    -- the inline box used for the smaller running header.
    document.meta['titlepage-title'] = title
    document.meta['titlepage-ltr'] = true
  end
  return document
end
