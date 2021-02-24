<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
	xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0">

	<xsl:template match="/">
		<xsl:processing-instruction name="xml-stylesheet">
			href="asvs.xsl" type="text/xsl"
		</xsl:processing-instruction>

		<asvs>
			<xsl:apply-templates select="//table:table[position()&lt;=14]"
				mode="asvs" />
		</asvs>
	</xsl:template>

	<xsl:template match="table:table" mode="asvs">
		<category id="V{position()}">
			<name>
				<xsl:value-of select="preceding-sibling::text:p[position()=1]" />
			</name>
			<xsl:apply-templates select="table:table-row[position()&gt;1]"
				mode="asvs" />
		</category>
	</xsl:template>

	<xsl:template match="table:table" mode="html">
		<h1>
			<xsl:value-of select="preceding-sibling::text:p[position()=1]" />
		</h1>
		<table name="{@table:name}" border="1">
			<xsl:apply-templates select="table:table-row"
				mode="html" />
		</table>
	</xsl:template>

	<xsl:template match="table:table-row" mode="asvs">
		<item
			id="V{count(parent::*/preceding-sibling::table:table)+1}.{position()}">
			<xsl:apply-templates select="table:table-cell"
				mode="asvs" />
		</item>
	</xsl:template>

	<xsl:template match="table:table-row" mode="html">
		<tr name="{position()}">
			<xsl:apply-templates select="table:table-cell"
				mode="html" />
		</tr>
	</xsl:template>

	<xsl:template match="table:table-cell" mode="html">
		<xsl:choose>
			<xsl:when test="position()=1">
				<td>
					<xsl:value-of select="count(parent::*/preceding-sibling::*)-3" />
				</td>
				<td>
					<xsl:value-of select=".//text:p/text()" />
				</td>
			</xsl:when>
			<xsl:otherwise>
				<td level="{position()}">
					<xsl:choose>
						<xsl:when test="text:p/text()='&#xF0FC;'">
							x
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="text:p/text()" />
						</xsl:otherwise>
					</xsl:choose>
				</td>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template match="table:table-cell" mode="asvs">
		<xsl:choose>
			<xsl:when test="position()=1">
				<description>
					<xsl:value-of select=".//text:p/text()" />
				</description>
			</xsl:when>
			<xsl:otherwise>
				<include level="{position()-1}">
					<xsl:choose>
						<xsl:when test="text:p/text()='&#xF0FC;'">
							true
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="text:p/text()" />
						</xsl:otherwise>
					</xsl:choose>
				</include>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

</xsl:stylesheet>