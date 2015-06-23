https://wiki.duraspace.org/display/DSPACE/TechnicalFAQ#TechnicalFAQ-HowcanIchangewhatisdisplayedinXMLUIforaparticularcollection?

If you want items in a particular collection to be rendered differently (add/remove/modify elements) than in the rest of the repository, you can use this recipe.
<xsl:variable name='mycollection'><xsl:value-of select="/dri:document/dri:meta/dri:pageMeta/dri:trail[@target='/handle/123456789/1234']"/></xsl:variable>

```xml 
<xsl:template ...>
    ...
 
    <xsl:if test="$mycollection">
        <p>This item belongs to collection 123456789/1234.</p>
    </xsl:if>
 
    ...
</xsl:template>
```xml
