import c4d
from c4d import gui

def main():
    curDoc = c4d.documents.GetActiveDocument()
    docName = curDoc.GetDocumentName()      # get doc name
    docDir = curDoc.GetDocumentPath()       # get path
    docDir = docDir.replace("\\","/")       # reverse \ to /
    docDir = docDir+"/"                     # add another / at the end
    docPath = docDir+docName
    renderInfo = curDoc.GetActiveRenderData()
    beautyDir = renderInfo[c4d.RDATA_PATH]
    beautyDir = beautyDir.replace("\\","/")
    beautyFile = beautyDir.split("/")
    beautyFile = beautyFile[len(beautyFile)-1]
    beautyDir = beautyDir.replace(beautyFile,"")
    beautyPath = beautyDir+beautyFile
    multiDir = renderInfo[c4d.RDATA_MULTIPASS_FILENAME]
    multiDir = multiDir.replace("\\","/")
    multiFile = multiDir.split("/")
    multiFile = multiFile[len(multiFile)-1]
    multiDir = multiDir.replace(multiFile,"")
    multiPath = multiDir+multiFile
    
    #== METHODS ==#
    def get_version(string):
        v = string.split('.')
        v = v[len(v)-2]        # remove extension
        import math
        version = []
        for i in range(len(v)):
            try:
                x = int(v[i])
                version.append(x)
            except:
                pass
            i+=1
        if len(version)>0:
            version = ''.join(str(e) for e in version)    # convert list-integers to string
            version = 'v'+version
            return version
    # Increment All
    def incr_all(dV):
        # - increment and save document
        # - match render-output name's versions to doc-name
        #c4d.CallCommand(600000035) # Save and Increment document
        return True
    # Match Document Version
    def match_docVersion(dV):
        # - match render-output name's versions to doc-name
        bV = beautyFile.replace(beautyVersion,docVersion)
        mV = multiFile.replace(multiVersion,docVersion)
        beautyPath = beautyDir+bV
        multiPath = multiDir+mV
        renderInfo[c4d.RDATA_PATH] = beautyPath
        renderInfo[c4d.RDATA_MULTIPASS_FILENAME] = multiPath
        return [beautyPath,multiPath]
    #__INIT__#
    c4d.CallCommand(13957) # clear console
    docVersion = get_version(docName)
    beautyVersion = get_version(beautyFile)
    multiVersion = get_version(multiFile)
    print "o l d:"
    print beautyPath
    print multiPath
    new_versions = match_docVersion(docVersion)
    beautyPath = renderInfo[c4d.RDATA_PATH]
    multiPath = renderInfo[c4d.RDATA_MULTIPASS_FILENAME]
    print "n e w:"
    print beautyPath
    print multiPath

if __name__=='__main__':
    main()