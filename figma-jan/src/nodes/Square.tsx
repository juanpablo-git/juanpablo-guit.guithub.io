import { NodeProps,Handle, Position, NodeToolbar, NodeResizer } from "reactflow";

export function Square(pros:NodeProps){
    return(
        <div style={{backgroundColor:"violet",width:"auto" ,minWidth:200,minHeight:200,height:"100%"}}>
            
            <NodeResizer isVisible={pros.selected} minWidth={200} minHeight={200} />
            <Handle id="rigth" type="source" position={Position.Right} />
            <Handle id="left" type="target" position={Position.Left} />

        </div>
    )
}