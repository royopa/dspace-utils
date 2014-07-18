http://ucispace.lib.uci.edu/community-list

http://ugspace.ug.edu.gh/


Dear all,
i need help on how to incorporate AddThis Share Buttons in Dspace 1.8
Thanks

-- 
Sincerely Yours,

Henry Atsu Agbodza
Library Systems and Research Support, 
Academic Computing Unit,
University of Ghana Computing Systems (UGCS)
Room G3, Ground Floor - East Wing, 
Balme Library
Legon
Tel.: +233 (0) 207 027360
IP Phone: 2442

UG Digital Collection (UGSpace)
UG Library
UG Online Catalogue (UGCat)
UG Research Portal
UG Off - Campus Access to E - Resources
UG Chat with A Librarian Service

Henry,
I have the AddThis button on our DSpace instance here at the University of California, Irvine (http://ucispace.lib.uci.edu) appearing on every page, and my method for adding it is detailed below.
 
1.       Add something like this to sitemap.xmap for each theme you want to include the share button on:

 
<map:parameter name="javascript#3" value="http://s7.addthis.com/js/250/addthis_widget.js#username={your_addthis_user_id}"/> sitemap.xmap
 
2.       Add the AddThis namespace declaration to the top of page-structure.xsl (again, in each theme):

 
xmlns:addthis=http://www.addthis.com/help/api-spec
 
3.       I have a global variable called 'request-uri' but you can also reference this value directly from pageMeta in the DRI when creating the url value to share.  Remember to concatenate onto your full server path  (I actually use the full permalink/handle server path):

 
<xsl:variable name="request-uri" select="/dri:document/dri:meta/dri:pageMeta/dri:metadata[@element='request'][@qualifier='URI']" />
 
4.       Add something like this to page-structure.xsl where you want the button to appear (again, in each theme):

 
<!-- display share button -->
        <a>
            <xsl:attribute name="class">
                <xsl:text>addthis_button</xsl:text>
            </xsl:attribute>
            <xsl:attribute name="href">
                <xsl:text>http://www.addthis.com/bookmark.php?v=250&amp;pubid={your_addthis_pub_id}</xsl:text>
            </xsl:attribute>
            <xsl:attribute name="addthis:url">
                <xsl:value-of select="concat({full_server_path},{request_uri})"/>
            </xsl:attribute>
            <img>
                <xsl:attribute name="src">
                    <xsl:text>http://s7.addthis.com/static/btn/v2/lg-share-en.gif</xsl:text>
                </xsl:attribute>
                <xsl:attribute name="width">
                    <xsl:text>125</xsl:text>
                </xsl:attribute>
                <xsl:attribute name="height">
                    <xsl:text>16</xsl:text>
                </xsl:attribute>
                <xsl:attribute name="style">
                    <xsl:text>border:0;</xsl:text>
                </xsl:attribute>
                <xsl:attribute name="alt">
                    <xsl:text>Bookmark and Share</xsl:text>
                </xsl:attribute> 
            </img>
        </a>
 
 
--
Mark F. Vega
Programmer/Analyst
UC Irvine Libraries - Web Services
vegamf@uci.edu
949.824.9872
