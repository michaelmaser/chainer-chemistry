# -*- coding: utf-8 -*-
from chainer import functions

from chainer_chemistry.config import MAX_ATOMIC_NUM
from chainer_chemistry.links.readout.ggnn_readout import GGNNReadout
from chainer_chemistry.links.update.relgat_update import RelGATUpdate
from chainer_chemistry.models.graph_conv_model import GraphConvModel


class RelGAT(GraphConvModel):
    """Relational Graph Attention Networks (GAT)

    See: Veličković, Petar, et al. (2017).\
        Graph Attention Networks.\
        `arXiv:1701.10903 <https://arxiv.org/abs/1710.10903>`\
        Dan Busbridge, et al. (2018).\
        Relational Graph Attention Networks
        `<https://openreview.net/forum?id=Bklzkh0qFm>`\


    Args:
        out_dim (int): dimension of output feature vector
        hidden_dim (int): dimension of feature vector
            associated to each atom
        n_layers (int): number of layers
        n_atom_types (int): number of types of atoms
        n_heads (int): number of multi-head-attentions.
        n_edge_types (int): number of edge types.
        dropout_ratio (float): dropout ratio of the normalized attention
            coefficients
        negative_slope (float): LeakyRELU angle of the negative slope
        softmax_mode (str): take the softmax over the logits 'across' or
            'within' relation. If you would like to know the detail discussion,
            please refer Relational GAT paper.
        concat_hidden (bool): If set to True, readout is executed in each layer
            and the result is concatenated
        concat_heads (bool) : Whether to concat or average multi-head
            attentions
        weight_tying (bool): enable weight_tying or not

    """
    def __init__(self, out_dim, hidden_dim=16, n_heads=3, negative_slope=0.2,
                 n_edge_types=4, n_layers=4, dropout_ratio=-1.,
                 activation=functions.identity, n_atom_types=MAX_ATOMIC_NUM,
                 softmax_mode='across', concat_hidden=False,
                 concat_heads=False, weight_tying=False, with_gwm=False):
        # TODO: activation, softmax_mode, concat_heads
        # TODO: consider in_channels when concat_heads is True
        super(RelGAT, self).__init__(
            update_layer=RelGATUpdate, readout_layer=GGNNReadout,
            out_dim=out_dim, n_layers=n_layers,
            in_channels=hidden_dim, n_heads=n_heads,
            n_atom_types=n_atom_types, concat_hidden=concat_hidden,
            weight_tying=weight_tying, dropout_ratio=dropout_ratio,
            n_edge_types=n_edge_types, negative_slope=negative_slope,
            with_gwm=with_gwm
        )
