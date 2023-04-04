import React, { useCallback } from 'react';
import ReactFlow, { addEdge, Connection, ConnectionMode, Controls, Node, NodeToolbar, useEdgesState, useNodesState } from 'reactflow';

import 'reactflow/dist/style.css';
import DefaltEdges from './adges/DefaltEdge';
import { Square } from './nodes/Square';

const NODE_TYPES = {
  square: Square
}
const INICIAL_NODES = [{
  id: crypto.randomUUID(),
  type: "square",
  position: {
    x: 200,
    y: 400
  },
  data: {

  }

},
{
  id: crypto.randomUUID(),
  type: "square",
  position: {
    x: 600,
    y: 400
  },
  data: {

  }

}]satisfies Node[]

const EDGE_TYPES = {
  defalt: DefaltEdges,
}

const initialEdges = [{ id: 'e1-2', source: '1', target: '2' }];

export default function App() {
  const [edges, setEdges, onEdgesChange] = useEdgesState([])
  const [nodes, setNodes, onNodesCange] = useNodesState(INICIAL_NODES)
  const onConenect = useCallback((connection: Connection) => {
    return setEdges(edges => addEdge(connection, edges))
  }, [])

  function addSquareNode() {
    setNodes(nodes=>[...nodes,{
      id: crypto.randomUUID(),
      type: "square",
      position: {
        x: 200,
        y: 400
      },
      data: {
    
      }
    
    }])
    
  }
  return (
    <>

      <div style={{ width: '100vw', height: '100vh' }}>
      <div style={{ position: 'absolute', left: 10, top: 10, zIndex: 4 }}>
        <div>
          <label htmlFor="ishidden">
           <button onClick={addSquareNode}>+</button>
          </label>
        </div>
      </div>
        <ReactFlow
          nodeTypes={NODE_TYPES}
          nodes={nodes}
          edgeTypes={EDGE_TYPES}
          defaultEdgeOptions={{ type: 'defalt' }}
          connectionMode={ConnectionMode.Loose}
          edges={edges}
          onEdgesChange={onEdgesChange}
          onNodesChange={onNodesCange}
          onConnect={onConenect}
        >
          <Controls />
        </ReactFlow>
      </div>
    </>

  );
}