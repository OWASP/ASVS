<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:variable name="level_from" select="1" />
	<xsl:variable name="level_to" select="6" />

	<xsl:template match="/">
		<html>
			<head>
				<title>ASVS Checklist</title>
			</head>
			<body>
				<h1>ASVS Checklist</h1>
				<xsl:apply-templates select="asvs/category" />
			</body>
		</html>
	</xsl:template>

	<xsl:template match="category">
		<h2>
			<xsl:value-of select="name" />
		</h2>
		<table cellspacing="0" cellpadding="2" border="1">
			<tr><th>#</th><th>Description</th><th>1A</th><th>1B</th><th>2A</th><th>2B</th><th>3</th><th>4</th></tr>
			<xsl:apply-templates
				select="item[include[@level&gt;=$level_from and @level&lt;=$level_to]='true']" />
		</table>
	</xsl:template>

	<xsl:template match="item">
		<tr>
			<xsl:apply-templates select="description|include" />
		</tr>
	</xsl:template>

	<xsl:template match="include">
		<td width="10" align="center">
			<xsl:if test="text()='true'">
				x
			</xsl:if>
		</td>
	</xsl:template>

	<xsl:template match="description">
		<td>
			<xsl:value-of select="../@id" />
		</td>
		<td>
			<xsl:value-of select="." />
		</td>
	</xsl:template>

</xsl:stylesheet>