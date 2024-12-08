# NNterface

---
Visible: False
Date: 2024-12-03
---
<style>
    html {
        background-color: #FFFCF0 !important;
    }
    html.dark-mode {
        background-color: #111211 !important;
    }
</style>

# Introduction

<img src="../static/images/animation.gif" alt="Animated tiles" width="500" loading="lazy">

This post is a writeup for ongoing work on designing a whitebox interface for interacting with AI systems.

Motivation 

The Monitor research demo from Transluce deployed a model investigator AI system for actively understanding an LLM’s behavior. Their design centered around principles of empowering users, hand in hand with an AI investigator, to investigate fine grained model behavior.

[[illustration]] 

While chat interfaces are the primary method of interacting with AI systems, they’re ultimately more restrictive. They limit our understanding to an individual neuron level; I question: how might we allow users to deploy cutting edge interpretability on any model? 

Design and Principles

When designing no code interfaces, there’s careful balance between abstraction and detail. For example, block based programming languages are an intuitive way for kids to get started programming. Programming is like learning a language [citation needed]; offering structure, hierarchy, and prewritten components up front abstracts away the a lot of the learning curve. 

However, block based languages don’t fit well onto existing libraries. Toolkits like sklearn or pandas are an abstraction on top of existing languages - building block based systems directly onto existing abstractions doesn’t make sense. The difficulty of learning sklearn or pytorch is understanding all the arguments and options - code blocks don’t boil that away.

[[insert image of pytorch ml]]

Flow based editors are one solution. In Comfy UI, users design diffusion pipelines with drag and drop nodes. Pipelines can be as small as a couple nodes or scale to the complexity of a whole project. I found this an enticing approach and set out to design a similar system centered around the NNsight package [footnote link to walkthrough].

The Interface

Design

The interface is designed around NNsight - it primarily subgraphs between nodes to describe the context execution blocks used in the library. I’ll NNsight alongside visual components from the library to provide context for those who haven’t used it before. 

A Pytorch model consists of modules - named class attributes which are module objects are shown as members of the pytree. 

[[ image showing (left) raw pytree text (middle) dropdown with atomic names (right) cleaned pytree ]] 

NNsight wraps modules in the pytree with Envoys that expose an input and output property. Accessing the properties exposes proxies. Interactions between proxies within a trace context creates nodes on a graph – this is done by overriding magic methods on envoys. 

[[image showing input output envoy toggle]]

Dragging the node of one module to another, within a trace context, applies a directed get-> set operation. All operations are done within contexts. Contexts denote operations carried out in different forward passes of the model’s execution. 

[[show set operation]]

To minimize computation and execution cost, one may choose to batch traces together. In this case, an extra batch context allows operations to run at the same time. 

There are some default functions like basic arithmetic operations. Custom torch functions are available by expanding the code editor. Up to five inputs and one output are permitted for a block.

[[show functions, function editor]].

The interface comes with several predefined visualization blocks. A heatmap is useful for viewing patching effects per layer. A line graph is more effective for understanding the probability of certain tokens during the model’s predictions.

Building

I used svelte flow for the main drag and drop functionality.. Why Svelte? I just found it a lot more intuitive and fun to use than React.

The backend

How do I compile a visual language? Ultimately, I want to compile my visual abstraction of NNsight into raw nnsight code to be executed and results returned back to the user. Another benefit is that operations with the visual interface are easily exportable to raw NNsight to be run as Python.

The easiest solution is to perform a topological sort TS by dependencies. Consider the following graph: 

Executing TS on this graph returns the following node order.

[[node order, latex?]]

This doesn’t work. We forgot to include contexts in the graph. For each node, we set its parent to be its immediate context. However, TS  again on the nodes still doesn't work. The issue is that there’s no scope closure within context blocks. Later operations may interact with operations defined within a context block. We draw arrows between


Acknowledgements

Much thanks to Jaden Fiotto Kaufmann for building the NNsight library.  
