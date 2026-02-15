class PersistentSegTree:

    def __init__(self, V, reserve_nodes=0):
        self.N = V  
        self.L = [0]
        self.R = [0]
        self.CNT = [0]
        self.SUM = [0]
        if reserve_nodes > 0:
            self.L.extend([0] * reserve_nodes)
            self.R.extend([0] * reserve_nodes)
            self.CNT.extend([0] * reserve_nodes)
            self.SUM.extend([0] * reserve_nodes)

    # Clone node: make a new node identical to idx
    def clone(self, idx):
        self.L.append(self.L[idx])
        self.R.append(self.R[idx])
        self.CNT.append(self.CNT[idx])
        self.SUM.append(self.SUM[idx])
        return len(self.L) - 1

    # Update(prev_root, pos, delta_cnt, delta_sum)
    def update(self, prev_root, pos, delta_cnt, delta_sum):
        """
        Create a new version by adding (delta_cnt, delta_sum) at leaf `pos`.
        prev_root is previous version's root.
        """
        nl, nr = 1, self.N
        cur = prev_root
        stack = []

        # Descend to leaf
        while nl != nr:
            stack.append((cur, nl, nr))
            mid = (nl + nr) >> 1
            if pos <= mid:
                cur = self.L[cur]
                nr = mid
            else:
                cur = self.R[cur]
                nl = mid + 1

        # Clone leaf
        node = self.clone(cur)
        self.CNT[node] += delta_cnt
        self.SUM[node] += delta_sum

        # Clone back up
        while stack:
            prev_idx, l, r = stack.pop()
            new_node = self.clone(prev_idx)
            self.CNT[new_node] += delta_cnt
            self.SUM[new_node] += delta_sum

            mid = (l + r) >> 1
            if pos <= mid:
                self.L[new_node] = node
            else:
                self.R[new_node] = node

            node = new_node

        return node  # new root

    # kth(rootR, rootL, k)   rootR=roots[r], rootL=roots[l-1]
    def kth(self, rootL, rootR, k):
        """
        Return the compressed index of the k-th smallest element in
        the multiset (rootR - rootL).
        """
        nl, nr = 1, self.N
        curL, curR = rootL, rootR

        while nl != nr:
            mid = (nl + nr) >> 1
            left_count = self.CNT[self.L[curR]] - self.CNT[self.L[curL]]
            if k <= left_count:
                curR = self.L[curR]
                curL = self.L[curL]
                nr = mid
            else:
                k -= left_count
                curR = self.R[curR]
                curL = self.R[curL]
                nl = mid + 1

        return nl  # compressed index

    # query_count_sum(rootR, rootL, ql, qr)   rootR=roots[r], rootL=roots[l-1]
    def query_count_sum(self, rootL, rootR, ql, qr):
        """
        Returns (count, sum) of values whose compressed index ∈ [ql,qr]
        in the range represented by (rootR - rootL).
        Or: rootL se rootR tak k range mein kitne elements [ql,qr] k range
        mein h or unka summation kya h
        """
        if ql > qr:
            return (0, 0)

        stack = [(rootL, rootR, 1, self.N)]
        total_cnt = 0
        total_sum = 0

        while stack:
            rL, rR, nl, nr = stack.pop()
            if ql > nr or qr < nl:
                continue
            if ql <= nl and nr <= qr:
                total_cnt += self.CNT[rR] - self.CNT[rL]
                total_sum += self.SUM[rR] - self.SUM[rL]
                continue

            mid = (nl + nr) >> 1
            stack.append((self.R[rL], self.R[rR], mid + 1, nr))
            stack.append((self.L[rL], self.L[rR], nl, mid))

        return total_cnt, total_sum

    def range_total_count(self, rootL, rootR):
        return self.CNT[rootR] - self.CNT[rootL]

    def range_total_sum(self, rootL, rootR):
        return self.SUM[rootR] - self.SUM[rootL]

    '''
    Initialize as
    pst=PersistentSegTree(len(set(nums)))
    roots=[0]
    for i in range(n):
        roots.append(pst.update(roots[i],compressed_value_of_nums[i],1,nums[i]))
    Always compress with starting value 1 (sort the array and init a cnt)
    '''
